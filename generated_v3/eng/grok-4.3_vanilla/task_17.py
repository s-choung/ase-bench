from ase.build import bulk, surface
atoms = surface(bulk('Cu', 'fcc', a=3.6), (2, 1, 1), 3, vacuum=10)
print(len(atoms), atoms.cell)
