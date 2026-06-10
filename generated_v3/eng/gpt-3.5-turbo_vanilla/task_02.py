from ase import Atoms
from ase.build import fcc111
from ase.constraints import FixAtoms
from ase.calculators.emt import EMT
from ase.constraints import FixLinearCoord
from ase.constraints import FixAdsorbate
from ase.build import add_adsorbate
from ase.optimize import QuasiNewton

# Create Pt(111) 4-layer slab
slab = fcc111('Pt', size=(3, 3, 4), vacuum=10.0)

# Add CO molecule on ontop site
CO = Atoms('CO', positions=[(0., 0., 0.), (0., 0., 1.2)])
add_adsorbate(slab, CO, 1.7, 'ontop')

slab.calc = EMT()

# Print number of atoms
print(len(slab))
