from ase.build import fcc111, molecule, add_adsorbate, add_vacuum
from ase import Atoms

# Create Pt(111) 4-layer slab with vacuum
slab = fcc111('Pt', size=(3, 3, 4), vacuum=10.0)

# Add CO adsorbate on top site
co = molecule('CO')
add_adsorbate(slab, co, height=1.8, position='ontop')

# Print number of atoms
print(len(slab))
