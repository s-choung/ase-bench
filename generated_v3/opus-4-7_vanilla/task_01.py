from ase.build import bulk

cu = bulk('Cu', 'fcc', a=3.6) * (2, 2, 2)
print(cu.cell)
print(len(cu))
