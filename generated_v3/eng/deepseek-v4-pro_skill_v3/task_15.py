from ase.build import fcc100

# Build Cu(100) slab: 3 layers, 3x3 surface, 12 Å vacuum
slab = fcc100('Cu', size=(3,3,3), a=3.61, vacuum=12.0)

# Output basic information
print(f"Number of atoms: {len(slab)}")
cell_info = slab.get_cell_lengths_and_angles()
print(f"Cell lengths (Å): a={cell_info[0]:.3f}, b={cell_info[1]:.3f}, c={cell_info[2]:.3f}")
print(f"Cell angles (°): α={cell_info[3]:.1f}, β={cell_info[4]:.1f}, γ={cell_info[5]:.1f}")
