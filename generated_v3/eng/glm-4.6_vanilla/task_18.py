from ase.db import connect
from ase.geometry import get_distances
import numpy as np

db = connect('g2.db')
atoms = db.get_atoms(name='CH4')

print("Atomic coordinates (Å):")
for i, atom in enumerate(atoms):
    print(f"{atom.symbol:2s} {atom.position[0]:10.6f} {atom.position[1]:10.6f} {atom.position[2]:10.6f}")

print("\nBond lengths (Å):")
c_index = [i for i, atom in enumerate(atoms) if atom.symbol == 'C'][0]
h_indices = [i for i, atom in enumerate(atoms) if atom.symbol == 'H']
for h_index in h_indices:
    dist = np.linalg.norm(atoms[c_index].position - atoms[h_index].position)
    print(f"C-H: {dist:.6f}")

print(f"\nChemical formula: {atoms.get_chemical_formula()}")
