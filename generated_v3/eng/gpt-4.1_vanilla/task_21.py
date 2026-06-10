from ase.cluster.icosahedron import Icosahedron
from ase.calculators.emt import EMT
from ase import Atoms

# Create icosahedral Au nanoparticle with 3 shells
atoms = Icosahedron('Au', noshells=3)

# Assign a calculator (optional if you want energies/forces later)
atoms.calc = EMT()

# Output number of atoms
print('Number of atoms:', len(atoms))

# Output center of mass
print('Center of mass:', atoms.get_center_of_mass())
