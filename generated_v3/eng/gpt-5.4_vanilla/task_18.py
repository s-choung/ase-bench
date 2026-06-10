from ase.collections import g2
from ase.geometry import get_distances
import numpy as np

atoms = g2['CH4']

print("Chemical formula:", atoms.get_chemical_formula())
print("Atomic coordinates (Angstrom):")
for i, (sym, pos) in enumerate(zip(atoms.get_chemical_symbols(), atoms.positions)):
    print(f"{i:2d} {sym:2s} {pos[0]:10.6f} {pos[1]:10.6f} {pos[2]:10.6f}")

print("Bond lengths (Angstrom):")
symbols = atoms.get_chemical_symbols()
for i in range(len(atoms)):
    for j in range(i + 1, len(atoms)):
        d = atoms.get_distance(i, j)
        print(f"{i}-{j} ({symbols[i]}-{symbols[j]}): {d:.6f}")
