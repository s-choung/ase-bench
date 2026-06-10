from ase import Atoms
from ase.build import hcp_lattice

# Create HCP bulk structure for Ti
atoms = hcp_lattice("Ti", a=2.95, c_over_a=1.59)

# Print cell vectors and atomic positions
print("Cell vectors (Å):")
print(atoms.cell)
print("\nAtomic positions (Å):")
print(atoms.positions)
