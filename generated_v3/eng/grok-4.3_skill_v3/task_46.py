from ase import Atoms
from ase.build import fcc111, molecule, add_adsorbate
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms, FixBondLength
from ase.optimize import BFGS

slab = fcc111('Pt', size=(2,2,3), vacuum=10.0)
co = molecule('CO')
add_adsorbate(slab, co, 1.8, 'ontop')
c_idx, o_idx = len(slab) - 2, len(slab) - 1
fix_bot = FixAtoms(mask=[a.tag == 1 for a in slab])
fix_co = FixBondLength(c_idx, o_idx)
slab.set_constraint([fix_bot, fix_co])
slab.calc = EMT()
BFGS(slab).run(fmax=0.05)
print(slab.get_potential_energy(), slab.get_distance(c_idx, o_idx))
