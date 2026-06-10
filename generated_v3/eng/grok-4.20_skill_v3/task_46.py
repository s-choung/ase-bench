from ase import Atoms
from ase.build import fcc111, molecule, add_adsorbate
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms, FixBondLength
from ase.optimize import BFGS
from ase import units
import numpy as np

slab = fcc111('Pt', size=(4,4,3), vacuum=6.0)
co = molecule('CO')
add_adsorbate(slab, co, height=1.6, position='ontop')

slab.set_constraint([FixAtoms(mask=slab.get_tags() == 1),
                     FixBondLength(16, 17)])

slab.calc = EMT()
BFGS(slab).run(fmax=0.05)

e = slab.get_potential_energy()
d = slab.get_distance(16, 17)
print('Final energy:', e)
print('C-O distance:', d)
