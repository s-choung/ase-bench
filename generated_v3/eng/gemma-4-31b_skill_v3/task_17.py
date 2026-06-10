from ase.build import bulk, surface, add_vacuum

# Create bulk Cu
atoms_bulk = bulk('Cu', 'fcc', a=3.61)

# Cut surface (2,1,1) with 3 layers
slab = surface(atoms_bulk, (2, 1, 1), layers=3)

# Add 10 Angstroms of vacuum
add_vacuum(slab, 10.0)

print(f"Number of atoms: {len(slab)}")
print(f"Cell:\n{slab.get_cell()}")
