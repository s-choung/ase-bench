from ase.build import bulk

# Set HCP lattice parameters for Ti
a = 2.95
c = a * 1.59

# Generate Ti HCP bulk structure
ti_hcp = bulk('Ti', 'hcp', a=a, c=c)

# Print required structure data
print("Cell vectors (Å):\n", ti_hcp.cell)
print("\nAtomic Cartesian positions (Å):\n", ti_hcp.positions)
