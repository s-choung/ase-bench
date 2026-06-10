from ase.build import bcc110
from ase.io import write

# Create Fe BCC(110) surface
slab = bcc110('Fe', size=(2, 2, 4), vacuum=10.0)

# Print number of atoms
print(f"Number of atoms: {len(slab)}")

# Print cell sizes (a, b, c in Å)
cell_lengths = slab.get_cell_lengths_and_angles()[:3]  # First 3 are lengths
print(f"Cell sizes (Å): a={cell_lengths[0]:.2f}, b={cell_lengths[1]:.2f}, c={cell_lengths[2]:.2f}")

# Optional: Save to file
write('Fe_bcc110_surface.xyz', slab)
