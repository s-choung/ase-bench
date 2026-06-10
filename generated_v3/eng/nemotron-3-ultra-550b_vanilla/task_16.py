from ase.build import bcc110

# Create Fe BCC(110) surface
slab = bcc110('Fe', size=(2, 2, 4), vacuum=10.0)

# Print number of atoms and cell size
print(f"Number of atoms: {len(slab)}")
print(f"Cell size (Å): {slab.cell.lengths()}")
