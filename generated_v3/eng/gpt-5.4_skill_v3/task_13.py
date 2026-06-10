from ase.build import bulk

atoms = bulk('Si', 'diamond', a=5.43, cubic=True)
atoms = atoms * (3, 3, 3)

print('Number of atoms:', len(atoms))
print('Cell volume (A^3):', atoms.get_volume())
