from ase import Atoms
from ase.data import covalent_radii
from ase.collections import g2
import numpy as np

atoms = g2('CH4')

print("Atomic Coordinates:")
for i, atom in enumerate(atoms):
    print(f"Atom {i+1}: Symbol={atom.symbol}, Position={atom.position}")

print("\nBond Lengths:")
for i in range(len(atoms)):
    for j in range(i + 1, len(atoms)):
        distance = np.linalg.norm(atoms[i].position - atoms[j].position)
        print(f"Bond between {atoms[i].symbol} and {atoms[j].symbol}: {distance:.2f} Å")

print("\nChemical Formula:", atoms.get_chemical_formula())
