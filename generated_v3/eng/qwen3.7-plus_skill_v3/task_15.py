from ase.build import fcc100

slab = fcc100('Cu', size=(3, 3, 3), vacuum=12.0)

print("Number of atoms:", len(slab))
print("Cell info:")
print(slab.get_cell())
