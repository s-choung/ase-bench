from ase.build import fcc100

# Build Cu(100) slab with specified parameters
slab = fcc100('Cu', size=(3, 3, 3), vacuum=12.0)

# Print required information
print(f"Number of atoms in slab: {len(slab)}")
cell_lenghts_angles = slab.get_cell_lengths_and_angles()
print(f"Cell parameters [a(Å), b(Å), c(Å), α(°), β(°), γ(°)]: {cell_lenghts_angles.round(4)}")
