from ase.build import bcc110

atoms = bcc110('Fe', size=(2, 2, 4), vacuum=10, a=2.866)

print(f"Number of atoms: {len(atoms)}")
print(f"Cell size (a, b, c): {atoms.cell.lengths()}")
