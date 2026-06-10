from ase import Atoms
from ase.build import mx2

# Create MoS2 monolayer
mol = mx2('MoS2', kind='2H', a=3.18, thickness=1, vacuum=10)

# Print cell size
print(mol.cell_length_and_angle())  # Returns (a, b, c, α, β, γ)
