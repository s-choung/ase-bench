from ase.build import bulk, supercell

cu = bulk('Cu', 'fcc', a=3.6)
supercell = supercell(cu, (2, 2, 2))
print("Cell:")
print(supercell.cell)
print("Number of atoms:", len(supercell))
