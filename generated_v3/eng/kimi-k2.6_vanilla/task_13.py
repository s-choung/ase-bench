from ase.build import bulk

si = bulk('Si', 'diamond', a=5.43, cubic=True)
si *= [3, 3, 3]

print(len(si))
print(si.get_volume())
