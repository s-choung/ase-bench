from ase import Atoms
import numpy as np

# Create CO2 molecule
positions = [(0, 0, 0), (1.16, 0, 0), (-1.16, 0, 0)]  # C at origin, O at ±1.16 Å
atoms = Atoms('COO', positions=positions, cell=[10, 10, 10], pbc=False)

# Calculate interatomic distances
distances = atoms.get_distances(mic=False)
print(distances)
