from ase.cluster import Icosahedron
from ase.data import atomic_masses

# Create Au icosahedron with 3 shells
atoms = Icosahedron('Au', noshells=3)

# Print number of atoms
print(f"Number of atoms: {len(atoms)}")

# Calculate and print center of mass
masses = atomic_masses[atoms.get_atomic_numbers()]
com = (atoms.get_positions() * masses[:, None]).sum(axis=0) / masses.sum()
print(f"Center of mass: {com}")
