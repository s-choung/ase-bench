from ase.build import bulk

atoms = bulk('Cu', 'fcc').repeat((2, 2, 2))

print("Cell:\n", atoms.cell[:])
print("Number of atoms:", len(atoms))
