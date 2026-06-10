from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.neb import NEB
from ase.optimize import BFGS
from ase.geometry import find_mic
from ase.io import write
import numpy as np

a = 3.61
slab = fcc111('Cu', size=(2, 2, 4), a=a, vacuum=8.0)
zmax = slab.positions[:, 2].max()
mask = slab.positions[:, 2] < zmax - 1.0

def make_image(site):
    atoms = slab.copy()
    add_adsorbate(atoms, 'Cu', 1.8, position=site)
    atoms.set_constraint(FixAtoms(mask=mask))
    atoms.calc = EMT()
    return atoms

initial = make_image('fcc')
final = make_image('hcp')

images = [initial]
for _ in range(3):
    img = initial.copy()
    img.set_constraint(FixAtoms(mask=mask))
    img.calc = EMT()
    images.append(img)
images.append(final)

neb = NEB(images)
neb.interpolate(method='idpp')

opt = BFGS(neb, logfile=None)
opt.run(fmax=0.05)

energies = [img.get_potential_energy() for img in images]
barrier = max(energies) - energies[0]
print(barrier)
