from ase.build import bulk
from ase.geometry import find_mic
from ase import Atoms

# Define lattice parameters
a = 2.95
c_over_a = 1.59
c = a * c_over_a

# Create a Titanium HCP bulk structure
hcp_Ti = bulk('Ti', 'hcp', a=a, c=c)

# Print cell vectors
print("Cell Vectors:")
print(hcp_Ti.cell)

# Print atomic positions
print("\nAtomic Positions:")
for pos in hcp_Ti.get_scaled_positions():
    print(pos)
