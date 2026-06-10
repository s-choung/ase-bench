from ase.build import bulk

si_bulk = bulk('Si', 'diamond', a=5.43)
si_supercell = si_bulk.repeat((3, 3, 3))
print(si_supercell.get_number_of_atoms())
print(si_supercell.get_volume())
