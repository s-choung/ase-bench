from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.mep import NEB
from ase.optimize import BFGS
from ase.neb import interpolate
from ase.io import write
import numpy as np

slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0, orthogonal=True)
slab.calc = EMT()

z = slab.positions[:, 2].max()
fcc = (slab.cell[0, 0] / 3, slab.cell[1, 1] / 3)
hcp = (2 * slab.cell[0, 0] / 3, 2 * slab.cell[1, 1] / 3)

initial = slab.copy()
add_adsorbate(initial, 'Cu', 1.8, position=fcc)
initial.set_constraint(FixAtoms(indices=[a.index for a in initial if a.position[2] < z + 1e-6]))
initial.calc = EMT()

final = slab.copy()
add_adsorbate(final, 'Cu', 1.8, position=hcp)
final.set_constraint(FixAtoms(indices=[a.index for a in final if a.position[2] < z + 1e-6]))
final.calc = EMT()

images = [initial]
for _ in range(3):
    img = initial.copy()
    img.calc = EMT()
    images.append(img)
images.append(final)

neb = NEB(images)
neb.interpolate(method='idpp')

for img in images:
    img.calc = EMT()

opt = BFGS(neb, trajectory='neb.traj', logfile=None)
opt.run(fmax=0.05)

energies = [img.get_potential_energy() for img in images]
barrier = max(energies) - energies[0]
print(f"Energy barrier: {barrier:.6f} eV")
