from ase.build import bulk

cu_fcc = bulk('Cu', 'fcc')
supercell = cu_fcc * (2, 2, 2)
print('Cell information:\n', supercell.cell)
print('Number of atoms:', len(supercell))
