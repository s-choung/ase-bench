from ase.build import bulk

atoms = bulk('Cu', 'fcc', a=3.615, cubic=True)
supercell = atoms.repeat((2, 2, 2))

print("Cell:")
print(supercell.cell)
print("Number of atoms:", len(supercell))
