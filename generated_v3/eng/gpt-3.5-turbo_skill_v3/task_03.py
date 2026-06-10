from ase.build import mx2

# Create MoS2 monolayer structure with 10 angstrom vacuum
atoms = mx2('MoS2', kind='2H', a=3.18, thickness=3.17, vacuum=10)

# Print the cell size [a, b, c, α, β, γ]
print("Cell size:", atoms.get_cell_lengths_and_angles())
