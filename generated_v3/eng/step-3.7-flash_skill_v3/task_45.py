from ase.build import molecule
from ase.calculators.morse import MorsePotential
from ase.constraints import FixBondLength

atoms = molecule('H2')
atoms.calc = MorsePotential()

e_before = atoms.get_potential_energy()
d_before = atoms.get_distance(0, 1)

atoms.set_distance(0, 1, 0.9)
atoms.set_constraint([FixBondLength(0, 1)])

e_after = atoms.get_potential_energy()
d_after = atoms.get_distance(0, 1)

print(f'Before constraint: bond = {d_before:.2f} Å, E = {e_before:.4f} eV')
print(f'After constraint: bond = {d_after:.2f} Å, E = {e_after:.4f} eV')
