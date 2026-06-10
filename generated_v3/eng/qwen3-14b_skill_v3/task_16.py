from ase.build import bcc110
atoms = bcc110('Fe', size=(2, 2, 4), vacuum=10)
print(len(atoms))
print(atoms.get_cell_lengths_and_angles())
