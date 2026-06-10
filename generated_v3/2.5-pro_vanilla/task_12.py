from ase.build import hcp

# Define lattice parameters for Ti HCP
a = 2.95
c_over_a = 1.59
c = a * c_over_a

# Create the Ti HCP structure
ti_hcp = hcp(symbol='Ti', a=a, c=c)

# Print the cell vectors
print("Cell vectors (in Angstrom):")
print(ti_hcp.get_cell())

# Print the atomic positions
print("\nAtomic positions (in Angstrom):")
print(ti_hcp.get_positions())
