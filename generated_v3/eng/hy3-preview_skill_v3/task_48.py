from ase.build import bulk
from ase.geometry import get_distances

# Create 2x2x2 supercell of FCC Cu
atoms = bulk('Cu', 'fcc', a=3.6).repeat((2, 2, 2))

# Calculate distances from atom 0 to all others with MIC
distances = get_distances(atoms[0].position, atoms.get_positions(), 
                          cell=atoms.cell, pbc=atoms.pbc, mic=True)[1]

# Get min and max distances (excluding self-distance)
distances = distances[distances > 0]
print(f"Minimum distance: {distances.min():.3f} Å")
print(f"Maximum distance: {distances.max():.3f} Å")
