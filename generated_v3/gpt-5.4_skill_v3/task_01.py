from ase.build import bulk

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
supercell = atoms * (2, 2, 2)

print(supercell.get_cell())
print(len(supercell))
