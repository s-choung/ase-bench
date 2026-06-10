from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase import Atoms

# Create a Pt(111) slab with 4 layers and add a CO molecule on top
slab = fcc111('Pt', thickness=4, vacuum=10.0)
co_molecule = Atoms('CO')
add_adsorbate(slab, co_molecule, 'O', ads_pos='on-top')

# Assign a default calculator (EMT) for the slab
slab.calc = EMT()

# Print the number of atoms in the final structure
print(len(slab))
