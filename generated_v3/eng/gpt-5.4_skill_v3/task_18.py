from ase.build import molecule
from ase.geometry import get_distances
import numpy as np

atoms = molecule('CH4')

print('Coordinates (Angstrom):')
for i, atom in enumerate(atoms):
    x, y, z = atom.position
    print(f'{i:2d} {atom.symbol:2s} {x:10.6f} {y:10.6f} {z:10.6f}')

print('\nBond lengths (Angstrom):')
pos = atoms.get_positions()
symbols = atoms.get_chemical_symbols()
for i in range(len(atoms)):
    for j in range(i + 1, len(atoms)):
        d = np.linalg.norm(pos[i] - pos[j])
        print(f'{i}-{j} ({symbols[i]}-{symbols[j]}): {d:.6f}')

print('\nChemical formula:')
print(atoms.get_chemical_formula())
