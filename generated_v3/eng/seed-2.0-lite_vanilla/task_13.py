from ase.build import bulk

# Create diamond structure Si unit cell, expand to 3x3x3 supercell
si_supercell = bulk('Si', crystalstructure='diamond', a=5.43).repeat((3, 3, 3))

# Output required metrics
print(f"Number of atoms: {len(si_supercell)}")
print(f"Cell volume (Å³): {si_supercell.get_volume():.2f}")
