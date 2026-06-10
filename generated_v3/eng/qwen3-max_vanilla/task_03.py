from ase import Atoms
from ase.build import mx2

# Create MoS2 monolayer (2H phase, hexagonal)
mos2 = mx2(formula='MoS2', kind='2H', a=3.18, thickness=3.18, size=(1, 1, 1))

# Add 10 Å vacuum along z-axis
cell = mos2.get_cell()
cell[2, 2] += 10.0
mos2.set_cell(cell, scale_atoms=False)

# Print cell size
print(mos2.get_cell().lengths())
