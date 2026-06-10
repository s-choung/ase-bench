from ase.build import bulk
from ase.neighborlist import NeighborList
import numpy as np

# Create a 3x3x3 supercell of Cu
atoms = bulk('Cu', 'fcc', a=3.6, size=(3, 3, 3))

# Create a NeighborList
nl = NeighborList(atoms, cutoff=2.5)  # Adjust cutoff as needed

# Update the NeighborList
nl.build()

# Calculate the number of neighbors for each atom
num_neighbors = []
for atom in atoms:
    num_neighbors.append(len(atom.neighbors))

# Calculate the average coordination number
avg_coordination = np.mean(num_neighbors)

# Print the average coordination number
print(f"Average coordination number: {avg_coordination}")
