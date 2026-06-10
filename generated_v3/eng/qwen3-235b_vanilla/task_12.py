from ase import Atoms
from ase.build import bulk
from ase.visualize import view

# Create HCP Titanium structure with given lattice parameters
ti = bulk('Ti', 'hcp', a=2.95, c_over_a=1.59)

# Print cell vectors and atomic positions
print("Cell vectors:")
print(ti.get_cell())
print("Atomic positions (Cartesian):")
print(ti.get_positions())
