from ase.build import mx2

# Create MoS2 monolayer
atoms = mx2('MoS2', kind='2H', a=3.18, thickness=3.17, vacuum=10.0)

# Print cell size (a, b, c)
print(atoms.get_cell_lengths_and_angles()[:3])
