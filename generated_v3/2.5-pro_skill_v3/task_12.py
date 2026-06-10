from ase.build import bulk

# Define lattice parameters for HCP Ti
a = 2.95
c = a * 1.59

# Create the HCP Ti bulk structure
ti_hcp = bulk('Ti', 'hcp', a=a, c=c)

# Print the cell vectors
print("Cell vectors (Å):")
print(ti_hcp.get_cell())

# Print the atomic positions
print("\nAtomic positions (Å):")
print(ti_hcp.get_positions())
