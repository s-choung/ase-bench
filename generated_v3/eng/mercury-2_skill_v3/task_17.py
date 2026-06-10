from ase.build import bulk, surface, add_vacuum

# Cu bulk
cu = bulk('Cu', 'fcc', a=3.6)

# (2 1 1) surface with 3 layers
slab = surface(cu, (2, 1, 1), layers=3)

# add 10 Å vacuum along z
add_vacuum(slab, 10.0)

print("Number of atoms:", slab.get_number_of_atoms())
print("Cell vectors (Å):\n", slab.get_cell())
