from ase.build import fcc100
from ase.io import write

# Create Cu(100) surface with 3 layers, 3x3 surface units, and 3 layers (total layers=3)
# Note: The 'layers' parameter includes all atomic layers in the slab
slab = fcc100('Cu', size=(3, 3, 3), vacuum=12.0, periodic=True)

# Print number of atoms
print(f"Number of atoms: {len(slab)}")

# Print cell information
cell = slab.get_cell()
cell_params = slab.get_cell_lengths_and_angles()
print(f"Cell vectors (Angstrom):\n{cell}")
print(f"Cell parameters (a, b, c, α, β, γ): {cell_params}")

# Optional: Write to file for visualization
write('cu100_surface.xyz', slab)
