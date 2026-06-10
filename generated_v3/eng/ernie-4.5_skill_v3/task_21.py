from ase import Atoms
from ase.cluster import Icosahedron
from ase.geometry import center_of_mass

# Create Au icosahedron with 3 shells
atoms = Icosahedron('Au', noshells=3)

# Print number of atoms
print(f"Number of atoms: {len(atoms)}")

# Calculate and print center of mass
com = center_of_mass(atoms)
print(f"Center of mass: {com}")
