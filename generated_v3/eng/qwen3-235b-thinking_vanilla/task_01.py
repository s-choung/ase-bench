from ase.build import bulk

cu = bulk('Cu', 'fcc')
supercell = cu * (2, 2, 2)
print(supercell.cell)
print(len(supercell))
