from ase.build import bulk

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
supercell = atoms * (2, 2, 2)

print("Cell:")
print(supercell.get_cell())
print("Cell lengths and angles:", supercell.cell.cellpar())
print("Number of atoms:", len(supercell))
print("Volume:", supercell.get_volume())
