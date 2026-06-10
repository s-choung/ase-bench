from ase.build import molecule
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength

atoms = molecule('H2')
atoms.calc = EMT()

r0 = atoms.get_distance(0, 1)
e0 = atoms.get_potential_energy()

atoms.set_constraint(FixBondLength(0, 1))
atoms.set_distance(0, 1, 0.9, fix=0)

r1 = atoms.get_distance(0, 1)
e1 = atoms.get_potential_energy()

print(f"Before: bond length = {r0:.6f} Å, energy = {e0:.6f} eV")
print(f"After : bond length = {r1:.6f} Å, energy = {e1:.6f} eV")
