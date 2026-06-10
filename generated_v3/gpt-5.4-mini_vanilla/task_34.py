from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.neb import NEB
from ase.optimize import BFGS
from ase.constraints import FixAtoms
from ase.io import write
import numpy as np

slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0, periodic=True)
slab.calc = EMT()

z = slab.positions[:, 2].max()
add_adsorbate(slab, 'Cu', height=2.0, position='fcc')
initial = slab.copy()
initial.calc = EMT()

final = slab.copy()
add_adsorbate(final, 'Cu', height=2.0, position='hcp')
final.calc = EMT()

mask = [atom.tag > 1 for atom in initial]
initial.set_constraint(FixAtoms(mask=mask))
final.set_constraint(FixAtoms(mask=mask))

images = [initial]
for _ in range(3):
    img = initial.copy()
    img.calc = EMT()
    images.append(img)
images.append(final)

neb = NEB(images, climb=True)
neb.interpolate(method='idpp')

for img in images:
    img.calc = EMT()

opt = BFGS(neb, trajectory='neb.traj', logfile='neb.log')
opt.run(fmax=0.05)

energies = [img.get_potential_energy() for img in images]
barrier = max(energies) - energies[0]
print(f"Energy barrier: {barrier:.6f} eV")
