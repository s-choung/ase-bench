from ase.build import bulk

si = bulk('Si', 'diamond', a=5.43)
sc = si * (3, 3, 3)

print(f"Number of atoms: {len(sc)}")
print(f"Cell volume: {sc.get_volume():.2f} A^3")
