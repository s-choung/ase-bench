from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength
from ase.optimize import BFGS

atoms = Atoms('H2', positions=[[0, 0, 0], [0.9, 0, 0]])
atoms.calc = EMT()

print("Before constraint:")
print(f"Bond length: {atoms.get_distance(0, 1):.4f} Å")
print(f"Energy: {atoms.get_potential_energy():.6f} eV")

atoms.set_constraint(FixBondLength(0, 1))
opt = BFGS(atoms)
opt.run(fmax=0.01)

print("\nAfter constraint + optimization:")
print(f"Bond length: {atoms.get_distance(0, 1):.4f} Å")
print(f"Energy: {atoms.get_potential_energy():.6f} eV")
