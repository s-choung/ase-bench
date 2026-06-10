from ase.build import mx2, add_vacuum

# Create MoS2 monolayer
mos2 = mx2('MoS2', kind='2H', a=3.18, thickness=3.17)

# Add vacuum in the z-direction
add_vacuum(mos2, vacuum=10.0)

# Print the cell size
print(mos2.get_cell_lengths_and_angles())
