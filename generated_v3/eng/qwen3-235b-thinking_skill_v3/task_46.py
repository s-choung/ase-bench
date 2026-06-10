from ase import Atoms
from ase.build import fcc111, molecule, add_adsorbate
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms, FixBondLength
from ase.optimize import BFGS

slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)
co = molecule('CO')
add_adsorbate(slab, co, height=1.8, position='ontop')

mask = [atom.tag == 1 for atom in slab]
c_idx = next(i for i, a in enumerate(slab) if a.symbol == 'C')
o_idx = next(i for i, a in enumerate(slab) if a.symbol == 'O')

slab.set_constraint([FixAtoms(mask=mask), FixBondLength(c_idx, o_idx)])
slab.calc = EMT()
BFGS(slab, logfile=None).run(fmax=0.05)

energy = slab.get_potential_energy()
co_dist = slab.get_distance(c_idx, o_idx)
print(f"{energy:.6f} {co_dist:.6f}")
