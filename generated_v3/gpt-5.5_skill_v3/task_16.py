from ase.build import bcc110

slab = bcc110("Fe", size=(2, 2, 4), vacuum=10.0, a=2.866)

print("Number of atoms:", len(slab))
print("Cell:")
print(slab.cell)
print("Cell lengths and angles:", slab.get_cell_lengths_and_angles())
