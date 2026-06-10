from ase.build import mx2

# Create a MoS2 monolayer (2H phase) with 10 Å vacuum along the c‑axis
atoms = mx2('Mo', 'S', kind='2H', a=3.18, vacuum=10)

# Output the cell dimensions
print(atoms.get_cell())
