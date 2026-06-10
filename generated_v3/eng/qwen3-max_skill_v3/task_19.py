from ase import Atoms
from ase.geometry import get_distances

# Create CO2 molecule: C at origin, O at ±1.16 Å along x-axis
atoms = Atoms('CO2',
              positions=[[0.0, 0.0, 0.0],
                         [-1.16, 0.0, 0.0],
                         [1.16, 0.0, 0.0]],
              cell=[10, 10, 10],
              pbc=False)

# Calculate all interatomic distances
distances = get_distances(atoms.positions)[1]

# Print distances (in Å)
print(distances)
