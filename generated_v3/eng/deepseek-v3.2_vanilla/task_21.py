from ase.cluster import Icosahedron
from ase.visualize import view

# Create Au icosahedron nanoparticle
atoms = Icosahedron('Au', noshells=3)

# Print number of atoms and center of mass
print(f'Number of atoms: {len(atoms)}')
print(f'Center of mass: {atoms.get_center_of_mass()}')

# Optional visualization (commented out as requested)
# view(atoms)
