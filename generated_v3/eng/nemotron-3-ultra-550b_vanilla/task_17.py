from ase.build import bulk, surface

# Create Cu bulk (FCC)
cu_bulk = bulk('Cu', 'fcc', a=3.615)

# Create (2,1,1) surface with 3 layers and 10 Å vacuum
slab = surface(cu_bulk, (2, 1, 1), layers=3, vacuum=10.0)

# Output results
print(f"Number of atoms: {len(slab)}")
print("Cell:")
print(slab.cell)
