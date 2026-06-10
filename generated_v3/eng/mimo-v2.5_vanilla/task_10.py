from ase.cluster import Octahedron
import numpy as np

# Create Cu octahedron with length=5 (5 atoms along edge)
cluster = Octahedron('Cu', 5)

# Print results
print(f"Number of atoms: {len(cluster)}")
print(f"Positions shape: {cluster.get_positions().shape}")
