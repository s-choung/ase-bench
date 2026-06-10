from ase.build import bulk

a = 5.43
atoms = bulk('Si', 'diamond', a=a) * (3, 3, 3)

print(len(atoms))
print(atoms.get_volume())
