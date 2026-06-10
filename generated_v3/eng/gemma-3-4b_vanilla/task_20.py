from ase import Atoms
from ase.build import fcc111
import numpy as np

c = 2.0  # Carbon radius in Angstroms
a = 3.0  # Lattice constant in Angstroms
n = 6   # Number of hexagons
m = 6   # Number of layers

carbon_atoms = fcc111('Au', n=n, m=m, a=a, radius=c)
carbon_atoms.cell -= carbon_atoms.cell[0]  # Correct the cell vector

num_atoms = len(carbon_atoms)
print(f"Number of atoms: {num_atoms}")
print(f"Cell info: {carbon_atoms.cell}")
