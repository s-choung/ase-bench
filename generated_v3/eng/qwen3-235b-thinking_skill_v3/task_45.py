from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength

atoms = Atoms('H2', positions=[[0, 0, 0], [0, 0, 0.74]])
atoms.calc = EMT()
e0 = atoms.get_potential_energy()
d0 = atoms.get_distance(0, 1)

atoms.positions[1] = [0, 0, 0.9]
atoms.set_constraint(FixBondLength(0, 1, bondlength=0.9))
e1 = atoms.get_potential_energy()
d1 = atoms.get_distance(0, 1)

print(f"Before: bond = {d0:.4f} Å, energy = {e0:.4f} eV")
print(f"After:  bond = {d1:.4f} Å, energy = {e1:.4f} eV")
