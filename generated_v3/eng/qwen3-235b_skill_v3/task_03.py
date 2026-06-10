from ase.build import mx2
from ase import Atoms

# Create MoS2 monolayer
mos2 = mx2('MoS2', kind='2H', a=3.18, thickness=3.17)

# Add vacuum
mos2.center(vacuum=10, axis=2)

# Print cell size
print(mos2.get_cell_lengths_and_angles()[:3])
