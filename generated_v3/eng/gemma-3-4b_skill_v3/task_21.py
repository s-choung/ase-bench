from ase import Atoms
from ase.build import icosahedron
from ase.spacegroup import crystal
from ase.visualize import view
from ase.positions import atoms_to_positions

# Create an Au Icosahedron nanoparticle with noshells=3
cell = crystal('Au', icosahedron(), spacegroup=454, noshells=3)
atoms = Atoms(cell, positions=atoms_to_positions(cell))

# Print the number of atoms
num_atoms = len(atoms)
print(f"Number of atoms: {num_atoms}")

# Calculate and print the center of mass
center_of_mass = atoms.get_center_of_mass()
print(f"Center of mass: {center_of_mass}")

# Visualize the nanoparticle (optional)
# view(atoms)
