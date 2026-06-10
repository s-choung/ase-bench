from ase.build import bulk

si = bulk('Si', 'diamond', a=5.43)
si_super = si.repeat((3, 3, 3))
print(f"Number of atoms: {len(si_super)}")
print(f"Cell volume: {si_super.get_volume():.2f} Å³")
