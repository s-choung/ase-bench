from ase.build import bulk, make_supercell

atoms = bulk('Cu', 'fcc', a=3.6)
supercell = make_supercell(atoms, [[2, 0, 0], [0, 2, 0], [0, 0, 2]])
print("Cell info:\n", supercell.cell)
print("Number of atoms:", len(supercell))
