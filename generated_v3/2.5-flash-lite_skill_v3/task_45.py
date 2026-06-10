from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength
from ase.optimize import BFGS

# H2 분자 생성
atoms = Atoms('H2', positions=[(0, 0, 0), (0, 0, 0.74)],
              calculator=EMT())

# Constraint 적용 전 bond length와 에너지 계산
initial_bond_length = atoms.get_distance(0, 1)
initial_energy = atoms.get_potential_energy()
print(f"Before constraint: Bond length = {initial_bond_length:.4f} Å, Energy = {initial_energy:.4f} eV")

# FixBondLength constraint 적용 (0.9 Å)
constraint = FixBondLength(0, 1, length=0.9)
atoms.set_constraint(constraint)

# Constraint 적용 후 에너지 계산 (최적화 수행)
# BFGS optimizer를 사용하여 에너지를 최소화합니다.
# FixBondLength constraint가 적용되어 있으므로, 원자 위치는 변경되지 않고 에너지 계산만 수행됩니다.
# 만약 위치 최적화가 필요하다면, FixBondLength constraint를 제거하거나 다른 방식으로 접근해야 합니다.
# 여기서는 constraint가 적용된 상태에서의 에너지를 바로 계산합니다.
atoms.calc.reset() # 재계산을 위해 calculator를 초기화합니다.
final_energy = atoms.get_potential_energy()
final_bond_length = atoms.get_distance(0, 1) # constraint로 인해 변경되지 않음

print(f"After constraint: Bond length = {final_bond_length:.4f} Å, Energy = {final_energy:.4f} eV")
