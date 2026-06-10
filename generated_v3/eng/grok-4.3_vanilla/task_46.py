from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms, FixBondLength
from ase.optimize import BFGS
slab = fcc111('Pt', (2, 2, 3), vacuum=10.0)
add_adsorbate(slab, 'CO', 1.8, 'ontop')
bottom = [a.index for a in slab if a.tag == 1]
c_idx, o_idx = len(slab)-2, len(slab)-1
cons = [FixAtoms(indices=bottom), FixBondLength(c_idx, o_idx)]
slab.set_constraint(cons)
slab.calc = EMT()
BFGS(slab).run(fmax=0.05)
print(slab.get_potential_energy(), slab.get_distance(c_idx, o_idx))
