from ase.build import surface, add_vacuum

# Create Cu (2,1,1) surface with 3 layers
slab = surface('Cu', (2,1,1), 3)

# Add 10 angstroms of vacuum
add_vacuum(slab, 10)

# Print number of atoms and cell
print(f"Number of atoms: {len(slab)}")
print(f"Cell:\n{slab.cell}")
