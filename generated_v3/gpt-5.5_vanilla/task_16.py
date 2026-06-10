from ase.build import bcc110

slab = bcc110("Fe", size=(2, 2, 4), a=2.87, vacuum=10.0)

print("Number of atoms:", len(slab))
print("Cell lengths (Angstrom):", slab.cell.lengths())
print("Cell:")
print(slab.cell)
