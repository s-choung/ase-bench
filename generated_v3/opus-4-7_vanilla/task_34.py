from ase.build import fcc111, add_adsorbate
from ase.constraints import FixAtoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.neb import NEB
import numpy as np

def make_slab(site):
    slab = fcc111('Cu', size=(4,4,3), vacuum=10.0)
    add_adsorbate(slab, 'Cu', height=2.0, position=site)
    slab.set_constraint(FixAtoms(mask=[a.tag >= 2 for a in slab]))
    slab.calc = EMT()
    return slab

initial = make_slab('fcc')
BFGS(initial, logfile=None).run(fmax=0.05)

final = make_slab('hcp')
BFGS(final, logfile=None).run(fmax=0.05)

n_images = 5
images = [initial]
for i in range(n_images - 2):
    img = initial.copy()
    img.calc = EMT()
    images.append(img)
images.append(final)

neb = NEB(images)
neb.interpolate(method='idpp')

for img in images[1:-1]:
    img.calc = EMT()

opt = BFGS(neb, logfile=None)
opt.run(fmax=0.05)

energies = [img.get_potential_energy() for img in images]
barrier = max(energies) - energies[0]
print("Energies:", energies)
print(f"Barrier: {barrier:.4f} eV")
