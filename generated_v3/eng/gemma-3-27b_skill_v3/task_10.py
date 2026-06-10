from ase.cluster import Octahedron
import numpy as np

octahedron = Octahedron('Cu', length=5)
print(f"Number of atoms: {len(octahedron)}")
print(f"Positions shape: {octahedron.positions.shape}")
