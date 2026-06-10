from ase.build import mx2

# Create MoS2 monolayer
mos2 = mx2('MoS2', kind='2H', a=3.18, thickness=3.17, vacuum=10)

# Print cell dimensions
print("Cell size (a, b, c, alpha, beta, gamma):")
print(mos2.get_cell_lengths_and_angles())
