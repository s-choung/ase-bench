from ase import Atoms
from ase.build import fcc111, add_adsorbate
from ase.constraints import FixAtoms, FixBondLength
from ase.calculators.emt import EMT
from ase.optimize import BFGS

slab = fcc111('Pt', size=(3, 3, 3), vacuum=10.0)
slab = add_adsorbate(slab, 'CO', height=1.5, position='ontop')
slab.constraints = [FixAtoms(range(9)), FixBondLength(-2, -1)]
slab.calc = EMT()
BFGS(slab).run(fmax=0.05)
print(slab.get_potential_energy())
print(slab.get_distance(-2, -1))
