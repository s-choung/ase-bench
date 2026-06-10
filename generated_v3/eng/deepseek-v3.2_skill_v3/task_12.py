from ase import Atoms
import numpy as np

a = 2.95
c = a * 1.59
cell = [[a, 0, 0],
        [-a/2, a*np.sqrt(3)/2, 0],
        [0, 0, c]]
positions = [[0, 0, 0],
             [1/3, 2/3, 1/2]]
atoms = Atoms('Ti2', positions=positions, cell=cell, pbc=True)

print("Cell vectors (Å):")
for i, vec in enumerate(atoms.cell):
    print(f"  a{i+1}: {vec}")

print("\nAtomic positions (Å):")
for i, pos in enumerate(atoms.positions):
    print(f"  Ti{i}: {pos}")

print(f"\nLattice parameters: a={a:.3f} Å, c={c:.3f} Å, c/a={1.59}")
print(f"Volume: {atoms.get_volume():.3f} Å³")
