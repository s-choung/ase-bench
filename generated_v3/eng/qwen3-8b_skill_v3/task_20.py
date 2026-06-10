from ase.build import nanotube

atoms = nanotube(n=6, m=6, length=4, symbol='C')
print(f"Number of atoms: {len(atoms)}")
print("Cell:")
print(atoms.get_cell())
