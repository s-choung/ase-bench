from ase.cluster import Icosahedron
from ase import Atoms

# Create an Au icosahedron with noshells=3
atoms = Icosahedron('Au', length=3, noshells=3)

# Get the number of atoms
num_atoms = len(atoms)
print(f'Number of atoms: {num_atoms}')

# Compute and print the center of mass
center_of_mass = atoms.get_center_of_mass()
print(f'Center of mass: {center_of_mass}')
