from ase.build import nanotube

atoms = nanotube(6, 6, length=4, symbol='C')

print(f"Number of atoms: {len(atoms)}")
print(f"Cell:\n{atoms.cell}")
print(f"Cell lengths: {atoms.cell.lengths()}")
print(f"Cell angles: {atoms.cell.angles()}")
