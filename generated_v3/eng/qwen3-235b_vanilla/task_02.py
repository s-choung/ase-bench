from ase import Atoms
from ase.build import fcc111, add_adsorbate
from ase.visualize import view

# Create Pt(111) 4-layer slab with 10 Å vacuum
slab = fcc111('Pt', size=(1,1,4), vacuum=10)

# Add CO molecule on ontop site
add_adsorbate(slab, 'CO', height=1.2, position='ontop')

# Print number of atoms
print(len(slab))
