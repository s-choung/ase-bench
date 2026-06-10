from ase.build import bulk

cu = bulk('Cu', 'fcc')
cu_super = cu * (2, 2, 2)
print(cu_super.get_cell())
print(cu_super.get_cell_lengths_and_angles())
print(len(cu_super))
