import numpy as np
from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.mep import NEB
from ase.optimize import BFGS

slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0, orthogonal=True)
slab.calc = EMT()

a = slab.cell[0, 0]
fcc = (a / 3.0, a / 3.0)
hcp = (2.0 * a / 3.0, 2.0 * a / 3.0)

initial = slab.copy()
initial += slab[0:1].copy()
initial[-1].position = [fcc[0], fcc[1], slab.positions[:, 2].max() + 1.8]
initial[-1].tag = 0
initial.calc = EMT()

final = slab.copy()
final += slab[0:1].copy()
final[-1].position = [hcp[0], hcp[1], slab.positions[:, 2].max() + 1.8]
final[-1].tag = 0
final.calc = EMT()

images = [initial] + [initial.copy() for _ in range(5)] + [final]
neb = NEB(images)
neb.interpolate(method='idpp')

for img in images[1:-1]:
    img.calc = EMT()

BFGS(neb).run(fmax=0.05)

energies = np.array([img.get_potential_energy() for img in images])
barrier = energies.max() - energies[0]
print(barrier)
