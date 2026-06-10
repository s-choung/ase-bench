from ase.build import mx2

# Create MoS2 monolayer with 10 Å vacuum
atoms = mx2(formula='MoS2', kind='2H', a=3.16, thickness=3.172, vacuum=10.0)

print("Cell size (lengths & angles):", atoms.cell.lengths_and_angles())
