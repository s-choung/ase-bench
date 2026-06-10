from ase.build import bulk

atoms = bulk('Si', 'diamond', a=5.43)
atoms = atoms * (3, 3, 3)
print(len(atoms))
print(atoms.get_volume())
