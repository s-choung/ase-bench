from ase.cluster import Icosahedron
from ase import Atoms

atoms = Icosahedron('Au', noshells=3)
num_atoms = len(atoms)
com = atoms.get_center_of_mass()
print(f"Number of atoms: {num_atoms}")
print(f"Center of mass: {com}")
