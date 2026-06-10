from ase.build import fcc100

# Create Cu(100) surface
slab = fcc100('Cu', size=(3,3,3), vacuum=12)

# Print number of atoms and cell info
print(f"Number of atoms: {len(slab)}")
print(f"Cell lengths and angles: {slab.get_cell_lengths_and_angles()}")
