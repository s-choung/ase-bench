from ase.build import bcc110

# Create Fe BCC(110) surface
slab = bcc110('Fe', size=(2, 2, 4), vacuum=10.0)

# Output information
print(f"Number of atoms: {len(slab)}")
print(f"Cell size (a, b, c): {slab.get_cell_lengths_and_angles()[:3]}")
