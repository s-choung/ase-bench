from ase.build import bulk

atoms = bulk('Cu', 'fcc')
atoms = atoms.repeat((2, 2, 2))
cell = atoms.get_cell_lengths_and_angles()
print("Cell info:", cell)
print("Number of atoms:", len(atoms))
