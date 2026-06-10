from ase.build import molecule
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength

atoms = molecule('H2')
atoms.calc = EMT()

d_before = atoms.get_distance(0, 1)
e_before = atoms.get_potential_energy()
print(f"Before: bond length = {d_before:.3f} Å, energy = {e_before:.3f} eV")

atoms.set_distance(0, 1, 0.9, fix=0.5)
atoms.set_constraint(FixBondLength(0, 1))

d_after = atoms.get_distance(0, 1)
e_after = atoms.get_potential_energy()
print(f"After: bond length = {d_after:.3f} Å, energy = {e_after:.3f} eV")
