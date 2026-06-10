from ase.build import bulk

# Create diamond structure Si bulk with given lattice constant
si_bulk = bulk('Si', 'diamond', a=5.43)
# Create 3x3x3 supercell
supercell = si_bulk.repeat((3, 3, 3))

# Print required values
print(f"Number of atoms: {len(supercell)}")
print(f"Cell volume (Å³): {supercell.get_volume():.2f}")
