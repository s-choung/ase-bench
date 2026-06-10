from ase.build import mx2
from ase.geometry import wrap_positions, vacuum

# Create MoS2 monolayer structure
moss = mx2(formula='MoS2', a=None)

# Add vacuum of 10 Å along the z-direction
moss = moss.center(align=(0, 0, 0))
moss = wrap_positions(moss, (0, 0, 0.5))
moss.cell[2, 2] += 10
moss.center(vacuum=10, axis=2)

# Print the cell size
print(f'Cell size: {moss.cell}')
