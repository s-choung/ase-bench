from ase.build import bulk

# Create Si in diamond structure with lattice constant 5.43 Å
si = bulk('Si', 'diamond', a=5.43)

# Make 3x3x3 supercell
si_supercell = si * (3, 3, 3)

# Print results
print(f'Number of atoms: {len(si_supercell)}')
print(f'Cell volume: {si_supercell.get_volume():.2f} Å³')
