from ase.build import bulk

# Cu fcc bulk
cu = bulk('Cu', 'fcc', a=3.615)
print('Bulk cell:', cu.get_cell())
print('Bulk atoms:', len(cu))

# 2x2x2 supercell
cu_s = cu * (2, 2, 2)
print('Supercell cell:', cu_s.get_cell())
print('Supercell atoms:', len(cu_s))
