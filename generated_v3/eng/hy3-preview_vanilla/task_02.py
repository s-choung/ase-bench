from ase.build import fcc111, add_adsorbate
from ase import Atoms

# Create 4-layer Pt(111) slab with vacuum
slab = fcc111('Pt', size=(1,1,4), vacuum=10.0)

# Create CO molecule
co = Atoms('CO', positions=[(0,0,0), (0,0,1.43)])

# Adsorb CO on ontop site
add_adsorbate(slab, co, height=2.0, position='ontop')

# Print number of atoms
print(f"Number of atoms: {len(slab)}")
