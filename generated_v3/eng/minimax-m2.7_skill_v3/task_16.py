from ase.build import bcc110

atoms = bcc110('Fe', size=(2, 2, 4), vacuum=10)

print(f"Number of atoms: {len(atoms)}")
cell = atoms.get_cell_lengths_and_angles()
print(f"Cell dimensions (a, b, c, alpha, beta, gamma): {cell}")
