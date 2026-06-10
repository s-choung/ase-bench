from ase.build import bulk

si = bulk('Si', 'diamond', a=5.43, cubic=True)
si_super = si * (3, 3, 3)

print(f"Number of atoms: {len(si_super)}")
print(f"Cell volume: {si_super.get_volume():.4f} Å³")
