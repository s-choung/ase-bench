from ase.build import bulk
atoms = bulk('Cu', 'fcc')
sc = atoms * (2, 2, 2)
print(sc.cell)
print(len(sc))
