from ase.build import bulk

atoms = bulk('Cu', 'fcc', a=3.615)
atoms = atoms * (2, 2, 2)  # or atoms.repeat((2,2,2))

print('Cell:\n', atoms.get_cell())
print('Number of atoms:', len(atoms))
