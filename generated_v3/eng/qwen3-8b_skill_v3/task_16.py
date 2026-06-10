from ase.build import bcc110

atoms = bcc110('Fe', size=(2, 2, 4), vacuum=10.0)
print(f"Number of atoms: {len(atoms)}")
cell_lengths = atoms.get_cell_lengths_and_angles()[:3]
print(f"Cell lengths (a, b, c): {cell_lengths}")
