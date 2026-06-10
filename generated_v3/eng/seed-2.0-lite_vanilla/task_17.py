from ase.build import bulk, surface

# Create bulk fcc Cu, then cut (211) surface with 3 layers + 10Å vacuum
cu_bulk = bulk('Cu', 'fcc', a=3.615)
cu_slab = surface(cu_bulk, (2,1,1), layers=3, vacuum=10.0)

# Output required values
print(f"Number of atoms: {len(cu_slab)}")
print(f"Unit cell:\n{cu_slab.cell}")
