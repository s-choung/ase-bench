from ase import Atoms
from ase.lattice.cubic import FaceCenteredCubic
from ase.constraints import FixAtoms
import numpy as np

# Create Cu FCC 2x2x2 supercell
bulk = FaceCenteredCubic(symbol='Cu', latticeconstant=3.61, size=(2, 2, 2))

# Get distances from atom 0 to all other atoms with mic=True
distances = bulk.get_distances(0, range(len(bulk)), mic=True)

# Print min and max distances
print(f"Minimum distance: {np.min(distances):.4f} Å")
print(f"Maximum distance: {np.max(distances):.4f} Å")
