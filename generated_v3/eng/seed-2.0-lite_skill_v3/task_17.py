from ase.build import bulk, surface, add_vacuum

# Build fcc Cu bulk
cu_bulk = bulk('Cu', 'fcc', a=3.61)
# Cut (211) surface with 3 layers
slab = surface(cu_bulk, indices=(2,1,1), layers=3)
# Add 10 Å vacuum along z-axis
add_vacuum(slab, 10.0)

# Output required values
print(f"Number of atoms: {len(slab)}")
print("Unit cell (Å):\n", slab.cell)
