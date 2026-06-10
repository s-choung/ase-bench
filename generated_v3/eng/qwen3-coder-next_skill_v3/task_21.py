from ase.cluster import Icosahedron
from ase import Atoms

# Create Au icosahedron with 3 shells
atoms = Icosahedron('Au', noshells=3)

# Print number of atoms
print(f"Number of atoms: {len(atoms)}")

# Calculate and print center of mass (in Angstrom)
com = atoms.get_center_of_mass()
print(f"Center of mass: ({com[0]:.3f}, {com[1]:.3f}, {com[2]:.3f})")
