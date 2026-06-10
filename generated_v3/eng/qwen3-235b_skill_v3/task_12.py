from ase import Atoms
from ase.build import bulk

# Create HCP Ti with specified a and c/a ratio
ti_hcp = bulk('Ti', 'hcp', a=2.95, covera=1.59)

# Print cell vectors and atomic positions
print("Cell vectors (Å):")
print(ti_hcp.get_cell())
print("\nAtomic positions (Å):")
print(ti_hcp.get_positions())
