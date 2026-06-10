from ase.build import bulk

cu = bulk('Cu', 'fcc', a=3.61)
supercell = cu * (2, 2, 2)
print('Cell:', supercell.get_cell())
print('Number of atoms:', len(supercell))
