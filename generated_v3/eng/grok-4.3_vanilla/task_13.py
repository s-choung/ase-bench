from ase.build import bulk
atoms = bulk('Si', 'diamond', a=5.43, cubic=True) * (3, 3, 3)
print(len(atoms), atoms.get_volume())
