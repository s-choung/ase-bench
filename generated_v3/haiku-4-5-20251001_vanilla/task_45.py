from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength
from ase.optimize import BFGS

# H2 분자 생성
h2 = Atoms('H2', positions=[[0, 0, 0], [0.74, 0, 0]], cell=[10, 10, 10], pbc=False)
h2.set_calculator(EMT())

# constraint 적용 전
print("=== Before Constraint ===")
print(f"Initial bond length: {h2.get_distance(0, 1):.4f} Å")
print(f"Initial energy: {h2.get_potential_energy():.6f} eV")

# 최적화 (constraint 없음)
dyn = BFGS(h2, trajectory=None)
dyn.run(fmax=0.01)
print(f"Optimized bond length: {h2.get_distance(0, 1):.4f} Å")
print(f"Optimized energy: {h2.get_potential_energy():.6f} eV")

# constraint 적용
h2_constrained = Atoms('H2', positions=[[0, 0, 0], [0.74, 0, 0]], cell=[10, 10, 10], pbc=False)
h2_constrained.set_calculator(EMT())
constraint = FixBondLength(0, 1, 0.9)
h2_constrained.set_constraint(constraint)

print("\n=== With FixBondLength Constraint (0.9 Å) ===")
print(f"Bond length: {h2_constrained.get_distance(0, 1):.4f} Å")
print(f"Energy: {h2_constrained.get_potential_energy():.6f} eV")

# constraint 적용 후 최적화
dyn2 = BFGS(h2_constrained, trajectory=None)
dyn2.run(fmax=0.01)
print(f"After optimization - Bond length: {h2_constrained.get_distance(0, 1):.4f} Å")
print(f"After optimization - Energy: {h2_constrained.get_potential_energy():.6f} eV")
