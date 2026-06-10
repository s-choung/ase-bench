from ase import Atoms
from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.mep import NEB
from ase.io import Trajectory
import numpy as np

slab = fcc111('Cu', size=(4,4,4), vacuum=10.0)
slab.calc = EMT()
BFGS(slab).run(fmax=0.05)

ads = Atoms('Cu')
add_adsorbate(slab, ads, height=2.0, position='fcc')

initial = slab.copy()
initial.calc = EMT()
BFGS(initial).run(fmax=0.05)

final = initial.copy()
final.calc = EMT()
pos = final.get_positions()
# Move adatom (last atom) from fcc to hcp hollow
pos[-1][0] += initial.get_cell()[0,0] / 6.0
pos[-1][1] += initial.get_cell()[1,1] / (2 * np.sqrt(3))
final.set_positions(pos)
BFGS(final).run(fmax=0.05)

images = [initial] + [initial.copy() for _ in range(5)] + [final]
for image in images[1:-1]:
    image.calc = EMT()

neb = NEB(images, climb=True)
neb.interpolate(method='idpp')

opt = BFGS(neb, trajectory='neb.traj')
opt.run(fmax=0.05)

energies = [image.get_potential_energy() for image in images]
barrier = max(energies) - energies[0]
print(barrier)
