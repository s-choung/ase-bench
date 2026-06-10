from ase import Atoms
from ase.geometry import get_distances

# Create CO2 manually
atoms = Atoms('CO2', 
             positions=[(0, 0, 0), (-1.16, 0, 0), (1.16, 0, 0)],
             cell=[10, 10, 10], 
             pbc=False)

# Calculate interatomic distances
distances = atoms.get_distances(0, [1, 2])
print(f"C-O distances: {distances[0]:.3f} Å, {distances[1]:.3f} Å")

# Calculate all pairwise distances
all_distances = get_distances(atoms.get_positions())
print(f"\nDistance matrix (Å):")
print(all_distances[1])
