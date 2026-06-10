from ase.build import fcc100
from ase.io import write

# Create Cu(100) surface with 3 layers, 3x3 lateral size, and 12A vacuum
slab = fcc100('Cu', size=(3, 3, 3), vacuum=12.0)

# Output information
print(f"Number of atoms: {len(slab)}")
print(f"Cell info (lengths, angles): {slab.get_cell_lengths_and_angles()}")

# Optional: write to file
# write('Cu100.xyz', slab)
