from ase.build import molecule
from ase import Atoms

methane = molecule('CH4')
print('Chemical formula:', methane.get_chemical_formula())
print('Atomic coordinates:')
for atom in methane:
    print(atom.symbol, atom.position)
print('Bond lengths (C-H):')
for i in range(1, len(methane)):
    dist = methane.get_distance(0, i)
    print(f'C-H{i}: {dist:.3f} Å')
