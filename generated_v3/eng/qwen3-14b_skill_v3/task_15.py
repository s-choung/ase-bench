from ase.build import fcc100

slab = fcc100('Cu', size=(3, 3, 3), vacuum=12)
print(len(slab))
print(slab.get_cell_lengths_and_angles())
