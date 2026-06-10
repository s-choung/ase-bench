from ase.build import bulk

si = bulk('Si', 'diamond', a=5.43)
supercell = si.repeat((3, 3, 3))

print(len(supercell))
print(supercell.get_volume())
