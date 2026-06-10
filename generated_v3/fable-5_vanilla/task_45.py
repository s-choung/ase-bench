from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength
from ase.optimize import BFGS

atoms = Atoms('H2', positions=[[0, 0, 0], [0, 0, 0.9]])
atoms.calc = EMT()

print("=== Constraint 적용 전 ===")
print(f"Bond length: {atoms.get_distance(0, 1):.4f} A")
print(f"Energy: {atoms.get_potential_energy():.6f} eV")

atoms.set_constraint(FixBondLength(0, 1))
opt = BFGS(atoms, logfile=None)
opt.run(fmax=0.01)

print("=== Constraint 적용 후 (최적화 완료) ===")
print(f"Bond length: {atoms.get_distance(0, 1):.4f} A")
print(f"Energy: {atoms.get_potential_energy():.6f} eV")
