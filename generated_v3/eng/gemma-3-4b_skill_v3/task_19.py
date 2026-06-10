from ase import Atoms
from ase.spacegroup import crystal
from ase.build import fcc111
import numpy as np

# Create a CO2 molecule
atom_types = ([12, 16, 16])  # C, O, O
positions = np.array([
    [0.0, 0.0, 0.0],
    [1.16, 0.0, 0.0],
    [0.0, 1.16, 0.0]
])
atoms = Atoms(positions=positions, cell=np.eye(3), symbols=['C', 'O', 'O'],dirs=crystal('garvins', direct=True))

# Set the cell to a 10x10x10 box with periodic boundary conditions turned off
atoms.set_cell(np.eye(3) * 10, scale=1)
atoms.pbc = False

# Calculate interatomic distances
distances = get_distances(atoms)
print("Interatomic Distances:")
print(distances)
