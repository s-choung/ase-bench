from ase.build import mx2, add_vacuum

# Create MoS2 monolayer
atoms = mx2('MoS2', kind='2H', a=3.18, thickness=3.17, vacuum=0)

# Add 10 Å of vacuum in the z-direction
add_vacuum(atoms, 10)

# Print cell lengths
print(atoms.get_cell_lengths_and_angles()[:3])
