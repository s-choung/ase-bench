from ase.build import fcc111, add_adsorbate
from ase.constraints import FixAtoms
from ase.calculators.emt import EMT
from ase.mep import NEB
from ase.optimize import BFGS
from ase.atoms import Atoms
import numpy as np

slab = fcc111('Cu', size=(3, 3, 3), vacuum=10.0, orthogonal=True)
tags = np.repeat([0, 1, 2], 9)
slab.set_tags(tags)
mask = [atom.index for atom in slab if atom.tag < 2]
fix = FixAtoms(indices=mask)
slab.set_constraint(fix)

initial = slab.copy()
add_adsorbate(initial, 'Cu', 1.5, position='fcc', offset=(0.5, 0.5))
initial.set_tags(np.append(tags, 3))
initial.set_constraint(FixAtoms(indices=[a.index for a in initial if a.tag < 2]))

final = slab.copy()
add_adsorbate(final, 'Cu', 1.5, position='hcp', offset=(0.5, 0.5))
final.set_tags(np.append(tags, 3))
final.set_constraint(FixAtoms(indices=[a.index for a in final if a.tag < 2]))

images = [initial]
for _ in range(3):
    image = initial.copy()
    image.set_constraint(FixAtoms(indices=[a.index for a in image if a.tag < 2]))
    images.append(image)
images.append(final)

neb = NEB(images, climb=True)
neb.interpolate('idpp')
for image in images:
    image.calc = EMT()

opt = BFGS(neb, trajectory='diffusion.traj')
opt.run(fmax=0.05)

energies = [image.get_potential_energy() for image in images]
barrier = max(energies) - energies[0]
print(f"Energy barrier: {barrier:.4f} eV")
