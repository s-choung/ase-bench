from ase.cluster.icosahedron import Icosahedron
from ase.build import material
from ase.calculators.emt import EMT

# Parameters
element = 'Au'
noshells = 3

# Create Icosahedron nanoparticle
atoms = Icosahedron(material(element), noshells=noshells)
atoms.set_calculator(EMT())

# Output number of atoms and center of mass
print("Number of atoms:", len(atoms))
print("Center of mass:", atoms.get_center_of_mass())
