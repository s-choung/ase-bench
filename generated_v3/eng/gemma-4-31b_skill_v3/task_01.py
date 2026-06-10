from ase.build import bulk

atoms = bulk('Cu', 'fcc', a=3.61)
atoms = atoms * (2, 2, 2)

print(f"Cell: {atoms.get_cell()}")
print(f"Number of atoms: {len(atoms)}")
