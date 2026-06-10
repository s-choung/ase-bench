from ase.build import bulk

atoms = bulk('Cu', 'fcc', a=3.615)
atoms = atoms.repeat((2, 2, 2))

print("Cell:")
print(atoms.cell)
print("Number of atoms:", len(atoms))
