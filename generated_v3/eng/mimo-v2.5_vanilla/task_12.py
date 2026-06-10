from ase import Atoms
import numpy as np

a = 2.95
c_ratio = 1.59
c = a * c_ratio

cell = [
    [a, 0, 0],
    [-a / 2, a * np.sqrt(3) / 2, 0],
    [0, 0, c]
]

pos1 = [0, 0, 0]
pos2 = [a / 2, a * np.sqrt(3) / 6, c / 2]

atoms = Atoms(symbols='Ti2', positions=[pos1, pos2], cell=cell, pbc=True)

print("Cell vectors:")
print(np.array(cell))
print("\nAtomic positions (Cartesian):")
for i, atom in enumerate(atoms):
    print(f"Atom {i+1} ({atom.symbol}): {atom.position}")
