from ase.build import bcc110

slab = bcc110('Fe', size=(2, 2, 4), vacuum=10.0)
print(len(slab))
print(slab.get_cell_lengths_and_angles())
