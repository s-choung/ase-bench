from ase import Atoms
from ase.geometry import get_distances

# Define atomic positions: C at (0, 0, 0), O atoms at ±1.16 Å on the x-axis
positions = [[0.0, 0.0, 0.0], [1.16, 0.0, 0.0], [-1.16, 0.0, 0.0]]
symbols = ['C', 'O', 'O']

# Create the Atoms object with a 10x10x10 Å cell and no periodic boundary conditions
atoms = Atoms(symbols=symbols, positions=positions, cell=(10, 10, 10), pbc=False)

# Calculate and print the interatomic distances
distances = get_distances(atoms, indices1=[0], indices2=[1, 2])
print("Distances (C to O):", distances[0, :])  # Output distances from C to each O atom
