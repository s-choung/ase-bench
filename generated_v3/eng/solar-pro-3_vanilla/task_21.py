from ase import Atoms
from ase.cluster.icosahedron import Icosahedron

atoms = Icosahedron('Au', noshells=3)
atoms.center()
print(f"Number of atoms: {len(atoms)}")
print(f"Center of mass: {atoms.center_of_mass()}")
