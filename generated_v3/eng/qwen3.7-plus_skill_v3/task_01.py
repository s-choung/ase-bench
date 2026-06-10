from ase.build import bulk

atoms = bulk('Cu', 'fcc')
atoms = atoms.repeat((2, 2, 2))

print("Cell lengths and angles:", atoms.get_cell_lengths_and_angles())
print("Number of atoms:", len(atoms))
