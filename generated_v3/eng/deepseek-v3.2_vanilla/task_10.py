from ase.cluster import Octahedron
from ase.visualize import view
import numpy as np

# Create octahedron nanoparticle
atoms = Octahedron('Cu', 5)
print(f"Number of atoms: {len(atoms)}")
print(f"Positions shape: {atoms.positions.shape}")
