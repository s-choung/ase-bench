from ase.build import bulk
si = bulk('Si', 'diamond', a=5.43)
supercell = si * (3, 3, 3)
print(f"Number of atoms: {len(supercell)}")
print(f"Cell volume: {supercell.get_volume():.3f} Å³")
