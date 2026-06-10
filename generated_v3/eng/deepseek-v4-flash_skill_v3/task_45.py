from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength

atoms = Atoms('H2', positions=[(0, 0, 0), (0, 0, 0.7)])
atoms.calc = EMT()

d = atoms.get_distance(0, 1)
e = atoms.get_potential_energy()
print(f"Before: bond length = {d:.4f} Å, energy = {e:.4f} eV")

atoms.set_constraint(FixBondLength(0, 1))
atoms.positions[1, 2] = 0.9

d = atoms.get_distance(0, 1)
e = atoms.get_potential_energy()
print(f"After: bond length = {d:.4f} Å, energy = {e:.4f} eV")
