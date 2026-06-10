from ase.build import nanotube

atoms = nanotube(n=6, m=6, length=4)

print(f"Number of atoms: {len(atoms)}")
print(f"Cell info:\n{atoms.get_cell()}")
