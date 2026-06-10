from ase.build import nanotube
atoms = nanotube(n=6, m=6, length=4, symbol='C')
print(f"Atoms: {len(atoms)}")
cell = atoms.get_cell()
print(f"Cell vectors:\n{cell}")
print(f"Lengths/angles: {atoms.get_cell_lengths_and_angles()}")
