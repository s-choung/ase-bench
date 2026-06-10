from ase import Atoms
from ase.cluster.octahedron import Octahedron
import numpy as np

# Cu Octahedron with edge length 5 units
cu_oct = Octahedron('Cu', size=5)

# Print information
print('Number of atoms:', len(cu_oct))
print('Positions shape:', cu_oct.get_positions().shape)
