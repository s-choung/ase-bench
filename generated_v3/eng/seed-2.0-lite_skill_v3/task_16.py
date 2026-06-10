from ase.build import bcc110

# Create Fe BCC(110) surface with specified parameters
slab = bcc110('Fe', size=(2, 2, 4), vacuum=10.0)

# Print required output
print(f"Number of atoms: {len(slab)}")
print(f"Unit cell dimensions (Å):\n{slab.get_cell()}")
