from ase.build import bulk

si = bulk('Si', 'diamond', a=5.43, cubic=True)
si = si * (3, 3, 3)
print(f"Number of atoms: {len(si)}")
print(f"Cell volume: {si.get_volume():.4f} Å³")
