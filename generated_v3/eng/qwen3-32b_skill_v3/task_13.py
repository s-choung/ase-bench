from ase.build import bulk

# Create Si bulk with diamond structure
atoms = bulk('Si', 'diamond', a=5.43)

# Generate 3x3x3 supercell
supercell = atoms * (3, 3, 3)

# Output results
print(len(supercell))
print(supercell.get_volume())
