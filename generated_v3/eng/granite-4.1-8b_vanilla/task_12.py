from ase import Atoms
from ase.lattice.hexagonal import HCP

# Define the HCP bulk structure for Ti
a = 2.95  # lattice parameter a in Å
c_over_a = 1.59  # ratio c/a
atoms = HCP('Ti', latticeconstant=a, c_over_a=c_over_a)

# Print the cell vectors and atomic positions
print("Cell vectors (Å):")
print(atoms.cell)
print("\nAtomic positions (Å):")
print(atoms.positions)
