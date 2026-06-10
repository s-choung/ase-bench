from ase.build import bulk

atoms = bulk('Cu', 'fcc', a=3.6)
atoms = atoms * (2, 2, 2)

print(f"Number of atoms: {len(atoms)}")
print(f"Cell vectors:\n{atoms.get_cell()}")
print(f"Cell lengths and angles: {atoms.get_cell_lengths_and_angles()}")
