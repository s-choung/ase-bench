from ase.build import bulk, surface, add_vacuum

atoms = bulk('Cu', 'fcc', a=3.61)
slab = surface(atoms, (2, 1, 1), layers=3)
add_vacuum(slab, 10.0)
print(len(slab))
print(slab.get_cell())
