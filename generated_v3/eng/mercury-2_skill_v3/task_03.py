from ase.build import mx2, add_vacuum
from ase import units

# Create 2H MoS2 monolayer (default a≈3.18 Å)
atoms = mx2('MoS2', kind='2H', a=3.18, thickness=3.17)

# Add 10 Å vacuum along z
add_vacuum(atoms, 10.0)

# Print cell lengths (a, b, c) and angles (α, β, γ)
print('Cell (a, b, c, α, β, γ):', atoms.get_cell_lengths_and_angles())
