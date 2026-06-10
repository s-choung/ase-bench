from ase import Atoms
from ase.cluster import Icosahedron
from ase.thermo import OrientationalRelaxationFreezing
from ase import units

# Create a gold (Au) icosahedron nanoparticle with number of shells equal to 3
atoms = Icosahedron('Au', noshells=3)

# Calculate the number of atoms
num_atoms = len(atoms)

# Print number of atoms
print("Number of atoms:", num_atoms)

# Calculate and print the center of mass
center_of_mass = atoms.get_center_of_mass()
print("Center of mass:", center_of_mass)
