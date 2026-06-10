from ase.build import bulk

cu = bulk('Cu', 'fcc')
cu_supercell = cu * (2, 2, 2)

print("Cell info:")
print(cu_supercell.cell)
print("Number of atoms:", len(cu_supercell))
