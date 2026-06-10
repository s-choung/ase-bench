from ase.build import molecule
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength

atoms = molecule('H2')
atoms.calc = EMT()

d_before = atoms.get_distance(0, 1)
e_before = atoms.get_potential_energy()

atoms.set_distance(0, 1, 0.9, fix=0.5)
atoms.set_constraint(FixBondLength(0, 1))

d_after = atoms.get_distance(0, 1)
e_after = atoms.get_potential_energy()

print(f'bond length before: {d_before:.6f} Å')
print(f'energy before: {e_before:.6f} eV')
print(f'bond length after: {d_after:.6f} Å')
print(f'energy after: {e_after:.6f} eV')
