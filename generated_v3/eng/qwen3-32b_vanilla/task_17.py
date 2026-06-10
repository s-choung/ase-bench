from ase.build import bulk, surface

atoms = surface(bulk('Cu', 'fcc'), (2, 1, 1), 3, vacuum=10)
print(len(atoms))
print(atoms.cell)
