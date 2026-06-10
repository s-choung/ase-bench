from ase.cluster import Icosahedron
from ase.constraints import FixAtoms
from ase.build import make_supercell
from ase.visualize import view
from ase import Atoms, units

# Create Au icosahedron nanoparticle
atoms = Icosahedron('Au', noshells=3)
atoms.center(vacuum=10.0)  # Add vacuum around the nanoparticle

# Print number of atoms and center of mass
num_atoms = len(atoms)
com = atoms.get_center_of_mass()
print(f'Number of atoms: {num_atoms}')
print(f'Center of mass: {com}')

# Visualize the nanoparticle
view(atoms)
