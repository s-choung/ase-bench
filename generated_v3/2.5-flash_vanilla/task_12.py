from ase.build import hcp

# Lattice parameters for Ti HCP
a = 2.95
c_over_a = 1.59
c = a * c_over_a

# Create Ti HCP bulk structure
atoms = hcp(symbol='Ti', a=a, c=c)

# Print cell vectors
print("Cell vectors:")
print(atoms.get_cell())

# Print atomic positions
print("\nAtomic positions:")
print(atoms.get_positions())
