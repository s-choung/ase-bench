from ase.build import bulk

si = bulk('Si', 'diamond', a=5.43)
si *= (3, 3, 3)

print(f"Number of atoms: {len(si)}")
print(f"Cell volume: {si.get_volume():.2f} Å^3")
