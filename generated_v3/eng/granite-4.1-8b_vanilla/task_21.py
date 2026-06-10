from ase.io import read
from ase.cluster import Icosahedron
from ase.calculators.emt import EMT
from ase import Atoms

# Create an Au icosahedron with 3 shells
num_atoms = 13  # 3 shells: 1 + 6 + 6 = 13 atoms
atoms = Icosahedron('Au', num_atoms)

# Assign a dummy calculator (EMT) to compute properties
atoms.calc = EMT()

# Print the number of atoms
print("Number of atoms:", len(atoms))

# Calculate and print the center of mass
center_of_mass = atoms.get_center_of_mass()
print("Center of mass:", center_of_mass)
