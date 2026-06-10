from ase.build import bulk

# Create Si diamond structure primitive cell
si = bulk('Si', 'diamond', a=5.43)

# Make 3x3x3 supercell
si_supercell = si.repeat((3, 3, 3))

# Output number of atoms and cell volume
print(f"Number of atoms: {len(si_supercell)}")
print(f"Cell volume: {si_supercell.get_volume():.3f} Å^3")
