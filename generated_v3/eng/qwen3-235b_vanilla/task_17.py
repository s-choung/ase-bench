from ase import Atoms
from ase.build import surface
from ase.lattice.cubic import FaceCenteredCubic

# Create Cu bulk with FCC structure
cu = FaceCenteredCubic(symbol='Cu', size=(1,1,1))

# Cut (2,1,1) surface with 3 layers and add 游戏副本 vacuum
slab = surface(cu, indices=(2,1,1), layers=3, vacuum=10)

# Print number of atoms and cell
print(f"Number of atoms: {len(slab)}")
print(f"Cell:\n{slab.get_cell()}")
