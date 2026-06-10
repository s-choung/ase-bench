from ase.build import bulk

atoms = bulk('Cu', 'fcc', a=3.615)
atoms *= [2, 2, 2]

print(atoms.cell)
print(len(atoms))
