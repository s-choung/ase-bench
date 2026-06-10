from ase.build import mx2

# Create MoS2 monolayer (2H phase)
mol = mx2('MoS2', kind='2H')

# Add 10 Å of vacuum along the z-direction
mol.center(vacuum=10.0, axis=2)

# Print the cell dimensions
print(mol.get_cell())
