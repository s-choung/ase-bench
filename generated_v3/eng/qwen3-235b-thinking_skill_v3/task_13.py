from ase.build import bulk

si = bulk('Si', 'diamond', a=5.43)
supercell = si * (3, 3, 3)
print(supercell.get_global_number_of_atoms())
print(supercell.get_volume())
