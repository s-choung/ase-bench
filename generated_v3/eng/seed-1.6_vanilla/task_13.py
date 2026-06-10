from ase.build import bulk

si_bulk = bulk('Si', 'diamond', a=5.43)
supercell = si_bulk.repeat((3, 3, 3))
print(len(supercell))
print(supercell.get_volume())
