from ase import Atom, Crystal
from ase.latticehexagonal import hcp

a = 2.95
c_a_ratio = 1.59
c = a * c_a_ratio

# Create Ti HCP structure
ti_hcp = hcp('Ti', cell=(a, a, c), size=(1, 1, 1))

# Print cell vectors
print("Cell vectors (Å):")
print(ti_hcp.cell)

# Print atomic positions
print("
Atomic positions (fractional coordinates):")
print(ti_hcp.positions)
