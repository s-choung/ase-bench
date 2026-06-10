from ase.build import icosahedron
from ase.calculators.emt import EMT
import numpy as np

# Create Au icosahedron with 3 shells
atoms = icosahedron('Au', noshells=3, latticeconstant=4.08)

# Attach EMT calculator
atoms.calc = EMT()

# Print number of atoms and center of mass
print(f"Number of atoms: {len(atoms)}")
print(f"Center of mass: {atoms.get_center_of_mass()}")
