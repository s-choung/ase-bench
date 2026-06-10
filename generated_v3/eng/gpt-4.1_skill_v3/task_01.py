from ase.build import bulk
atoms = bulk('Cu', 'fcc', a=3.6)
supercell = atoms * (2, 2, 2)
cell = supercell.get_cell_lengths_and_angles()
print('Cell:', cell)
print('Number of atoms:', len(supercell))
