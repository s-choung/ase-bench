from ase.build import fcc100, add_vacuum
from ase import units

# Cu(100) slab: 3×3 surface, 3 atomic layers, 12 Å vacuum
slab = fcc100('Cu', size=(3, 3, 3), vacuum=0.0)  # vacuum added separately
add_vacuum(slab, 12.0)

print("Number of atoms :", slab.get_number_of_atoms())
print("Cell lengths (Å):", slab.get_cell_lengths_and_angles()[:3])
print("Cell angles (°):", slab.get_cell_lengths_and_angles()[3:])
