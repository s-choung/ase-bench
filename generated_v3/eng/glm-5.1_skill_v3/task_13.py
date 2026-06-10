from ase.build import bulk

si = bulk('Si', 'diamond', a=5.43)
si_sc = si.repeat((3, 3, 3))

print(f"Number of atoms: {len(si_sc)}")
print(f"Cell volume: {si_sc.get_volume():.4f} Å³")
