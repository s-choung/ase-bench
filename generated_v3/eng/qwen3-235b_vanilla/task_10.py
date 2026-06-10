from ase.cluster.trajectory import octahedron
from ase.build import add_adsorbate
import numpy as np

# Create a Cu octahedron with length 5
cu_octahedron = oct手段on('Cu', 5)

# Print number of atoms and shape of positions
print(len(cu_octahedron))
print(cu_octahedron.get_positions().shape)
