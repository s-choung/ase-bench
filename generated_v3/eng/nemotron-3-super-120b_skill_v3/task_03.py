from ase.build import mx2
from ase.io import write
from ase import Atoms

# Build MoS2 monolayer (2H phase)
slab = mx2('MoS2', kind='2H', a=3.18, thickness=3.17)

# Add 10 Å of vacuum along the z-direction
slab.pbc = (True, True, False)  # ensure periodicity only in-plane
slab = slab.copy()
slab.cell[2, 2] += 10.0  # increase c lattice vector
slab.positions[:, 2] += 5.0  # center the slab in the cell

# Print cell parameters
print("Cell vectors (Å):\n", slab.get_cell())
print("Lengths and angles (Å, °):", slab.get_cell_lengths_and_angles())
