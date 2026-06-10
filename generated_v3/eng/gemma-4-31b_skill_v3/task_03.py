from ase.build import mx2

# Create MoS2 monolayer (2H phase by default)
atoms = mx2('MoS2', vacuum=10.0)

# Print the cell dimensions
print(atoms.get_cell().lengths())
