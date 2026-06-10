from ase.build import nanotube

atoms = nanotube(6, 6, length=4)
print(f"Number of atoms: {len(atoms)}")
print(f"Cell: {atoms.cell[:]}")
