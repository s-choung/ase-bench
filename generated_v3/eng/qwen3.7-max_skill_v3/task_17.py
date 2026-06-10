from ase.build import bulk, surface

cu_bulk = bulk('Cu', 'fcc')
slab = surface(cu_bulk, (2, 1, 1), 3, vacuum=10.0)

print(f"Number of atoms: {len(slab)}")
print(f"Cell:\n{slab.get_cell()}")
