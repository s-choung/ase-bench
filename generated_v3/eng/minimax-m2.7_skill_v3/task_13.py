from ase.build import bulk

si_bulk = bulk('Si', 'diamond', a=5.43)
supercell = si_bulk * (3, 3, 3)

print(f"Number of atoms: {len(supercell)}")
print(f"Cell volume: {supercell.get_volume():.4f} Å³")
