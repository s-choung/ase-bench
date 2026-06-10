from ase.build import fcc100
from ase import Atoms

# Create Cu(100) surface with 3 layers, 3x3 supercell in x/y, 12 Å vacuum
slab = fcc100('Cu', size=(3, 3, 3), vacuum=12.0)

# Print number of atoms and cell info
print(f"Number of atoms: {len(slab)}")
cell = slab.get_cell_lengths_and_angles()
print(f"Cell lengths (a, b, c): {cell[0]:.2f}, {cell[1]:.2f}, {cell[2]:.2f} Å")
print(f"Cell angles (α, β, γ): {cell[3]:.2f}°, {cell[4]:.2f}°, {cell[5]:.2f}°")
