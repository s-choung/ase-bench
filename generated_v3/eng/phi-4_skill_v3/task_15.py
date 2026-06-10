from ase.build import fcc100

# Create a Cu(100) surface with 3 layers
slab = fcc100('Cu', layers=3, size=(3, 3, 3), vacuum=12.0)

# Print the number of atoms in the slab
print("Number of atoms in the slab:", slab.get_number_of_atoms())

# Print cell information
cell_info = slab.get_cell()
print("Cell info:", cell_info)
