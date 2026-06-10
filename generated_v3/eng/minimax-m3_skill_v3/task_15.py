from ase.build import fcc100

slab = fcc100('Cu', size=(3, 3, 3), vacuum=12.0)

print(f"Number of atoms: {len(slab)}")
print(f"Cell:\n{slab.get_cell()}")
print(f"Cell lengths and angles (Å, °): {slab.get_cell_lengths_and_angles()}")
print(f"Periodic boundary conditions: {slab.pbc}")
