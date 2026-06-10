from ase.build import bulk, surface

# Create Cu bulk and cut (2,1,1) surface with 3 layers
cu_bulk = bulk('Cu', cubic=True)
slab = surface(cu_bulk, (2, 1, 1), 3)

# Add 10 angstroms of vacuum in z-direction
slab.center(vacuum=10, axis=2)

# Print results
print(f"Number of atoms: {len(slab)}")
print(f"Cell: {slab.cell}")
