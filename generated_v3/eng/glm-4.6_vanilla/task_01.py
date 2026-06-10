from ase.build import bulk

atoms = bulk('Cu', 'fcc')
supercell = atoms * (2, 2, 2)

print(supercell.cell)
print(len(supercell))
