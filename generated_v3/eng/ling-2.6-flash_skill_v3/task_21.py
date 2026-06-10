from ase.cluster import Icosahedron
from ase import Atoms

# Create Au icosahedron nanoparticle with 3 shells
atoms = Icosahedron('Au', 3)

# Print number of atoms
print(f"Number of atoms: {len(atoms)}")

# Print center of mass
com = atoms.get_center_of_mass()
print(f"Center of mass: {com}")
