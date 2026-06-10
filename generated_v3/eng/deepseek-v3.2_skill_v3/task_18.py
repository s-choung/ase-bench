from ase.build import molecule
from ase import Atoms
import numpy as np

atoms = molecule('CH4')

print("Formula:", atoms.get_chemical_formula())
print("Coordinates (Å):")
for i, atom in enumerate(atoms):
    pos = atom.position
    print(f"  {atom.symbol} {i}: {pos[0]:8.4f} {pos[1]:8.4f} {pos[2]:8.4f}")

distances = atoms.get_all_distances()
c_indices = [i for i, a in enumerate(atoms) if a.symbol == 'C']
h_indices = [i for i, a in enumerate(atoms) if a.symbol == 'H']
print("\nC-H bond lengths (Å):")
for h in h_indices:
    d = distances[c_indices[0], h]
    print(f"  C-H{h}: {d:.4f}")
