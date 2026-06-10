from ase.build import bulk, add_vacuum
from ase import Atoms

# Create MoS2 monolayer
mos2 = bulk('MoS2', '2H', a=3.16, layers=1)

# Add 10 Å vacuum in z-direction
add_vacuum(mos2, 10, axis=2)

# Print cell size
print(f"Cell size: {mos2.get_cell_lengths_and_angles()}")
