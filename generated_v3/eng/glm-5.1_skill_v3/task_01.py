from ase.build import bulk

cu = bulk('Cu', 'fcc', a=3.6)
cu_supercell = cu * (2, 2, 2)

print("Cell info:")
print(cu_supercell.cell)
print(f"Number of atoms: {len(cu_supercell)}")
