import ase
import ase.build
from ase.visualize import view
from ase.cluster import Cluster
from ase.io import write

# Build FCC bulk copper (5.4 Å lattice constant)
Cu = ase.build.bulk('Cu', 'fcc', a=5.4)

# Generate a 2x2x2 supercell
superC = Cu * 2 * 2 * 2

# Print cell information and atom count
print(superC)
print('Number of atoms:', len(superC))
