from ase.build import bulk

atoms = bulk('Cu', 'fcc', a=3.6)
atoms = atoms * (2, 2, 2)
print(atoms.get_cell())
print(len(atoms))
