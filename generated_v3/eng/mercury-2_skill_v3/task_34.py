from ase import Atom
from ase.build import fcc111, add_adsorbate
from ase.constraints import FixAtoms
from ase.calculators.emt import EMT
from ase.neb import NEB
from ase.optimize import BFGS
import numpy as np

# clean Cu(111) slab
slab = fcc111('Cu', size=(3, 3, 4), a=3.6, vacuum=10.0)
# fix bottom layer atoms
slab.set_constraint(FixAtoms(mask=[a.position[2] < slab.get_cell()[2, 2] * 0.2 for a in slab]))

# initial (fcc hollow) and final (hcp hollow) configurations
init = slab.copy()
add_adsorbate(init, Atom('Cu'), height=2.0, position='fcc')
final = slab.copy()
add_adsorbate(final, Atom('Cu'), height=2.0, position='hcp')

# NEB images (5 intermediate + endpoints)
images = [init] + [init.copy() for _ in range(5)] + [final]
for img in images:
    img.calc = EMT()

neb = NEB(images)
neb.interpolate(method='idpp')          # IDPP interpolation
opt = BFGS(neb)
opt.run(fmax=0.05, steps=200)           # relax NEB

energies = [img.get_potential_energy() for img in images]
barrier = max(energies) - energies[0]
print(f'Energy barrier: {barrier:.4f} eV')
