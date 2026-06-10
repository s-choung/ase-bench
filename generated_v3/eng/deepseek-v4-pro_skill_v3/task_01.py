from ase.build import bulk

cu = bulk('Cu', 'fcc', a=3.61, cubic=True)
supercell = cu.repeat((2, 2, 2))

print("Supercell cell (Å):")
print(supercell.get_cell())
print("Number of atoms:", len(supercell))
