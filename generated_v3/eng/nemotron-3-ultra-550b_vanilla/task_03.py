from ase.build import mx2
from ase import Atoms

# Create MoS2 monolayer (2H phase) without vacuum
mo_s2 = mx2(formula='MoS2', kind='2H', a=3.16, thickness=3.11, vacuum=0.0, size=(1, 1, 1))

# Add 10 Å vacuum along z-direction
mo_s2.center(vacuum=10.0, axis=2)

# Print cell size
print("Cell size (Å):", mo_s2.cell.lengths())
