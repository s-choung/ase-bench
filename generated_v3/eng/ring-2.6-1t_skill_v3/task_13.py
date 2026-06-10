from ase.build import bulk

si = bulk('Si', 'diamond', a=5.43)
si = si * (3, 3, 3)
print(len(si), si.get_volume())
