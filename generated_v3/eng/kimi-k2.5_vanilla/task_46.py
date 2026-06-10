from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms, FixBondLength
from ase.optimize import BFGS
from ase import Atoms

slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)
add_adsorbate(slab, Atoms('CO', [[0, 0, 0], [0, 0, 1.2]]), 2.0, 'fcc')
slab.set_constraint([FixAtoms(mask=[a.tag == 3 for a in slab]), FixBondLength(-2, -1)])
slab.calc = EMT()
BFGS(slab).run(fmax=0.05)
print(f'Energy: {slab.get_potential_energy():.4f} eV')
print(f'C-O distance: {slab.get_distance(-2, -1):.4f} Ang')
