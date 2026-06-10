from ase.build import bulk, surface, add_vacuum

cu_bulk = bulk('Cu', 'fcc', a=3.6)
slab = surface(cu_bulk, (2,1,1), layers=3)
add_vacuum(slab, vacuum=10.0, axis=2)

print(f"Number of atoms: {len(slab)}")
print(f"Cell: {slab.get_cell()}")
