from ase import Atoms
from ase.build import fcc111, add_adsorbate, add_vacuum
from ase.calculators.emt import EMT
import numpy as np

# Create a Pt(111) 4-layer slab
slab = fcc111('Pt', size=(2, 2, 4), vacuum=10.0)
slab.calc = EMT()

# Add a CO molecule on the ontop site
co = molecule('CO')
add_adsorbate(slab, co, height=1.8, position='ontop')

# Add vacuum
add_vacuum(slab, vacuum=10.0)

# Print the number of atoms in the final structure
num_atoms = len(slab)
print(num_atoms)
