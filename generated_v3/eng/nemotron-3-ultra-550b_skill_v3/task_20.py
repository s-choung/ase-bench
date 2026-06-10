from ase.build import nanotube

atoms = nanotube(6, 6, length=4.0, symbol='C')
print(f"Number of atoms: {len(atoms)}")
print(f"Cell: {atoms.get_cell()}")
print(f"Cell lengths and angles: {atoms.get_cell_lengths_and_angles()}")
