from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.mep import NEB
from ase.optimize import BFGS
import numpy as np

a = 3.6
slab0 = fcc111('Cu', size=(2, 2, 4), a=a, vacuum=10.0)
top_z = slab0.positions[:, 2].max()
top_inds = [i for i, p in enumerate(slab0.positions) if abs(p[2] - top_z) < 1e-6]
xy = slab0.positions[top_inds, :2]

center = xy.mean(axis=0)
d2 = ((xy - center) ** 2).sum(axis=1)
i0 = np.argmin(d2)
r0 = xy[i0]
others = [j for j in range(len(xy)) if j != i0]
others = sorted(others, key=lambda j: np.sum((xy[j] - r0) ** 2))[:6]
nbrs = xy[others]

angles = np.arctan2(nbrs[:, 1] - r0[1], nbrs[:, 0] - r0[0])
order = np.argsort(angles)
nbrs = nbrs[order]

fcc_xy = (r0 + nbrs[0] + nbrs[1]) / 3.0
hcp_xy = (r0 + nbrs[1] + nbrs[2]) / 3.0

def make_image(site_xy):
    slab = fcc111('Cu', size=(2, 2, 4), a=a, vacuum=10.0)
    add_adsorbate(slab, 'Cu', height=2.0, position=site_xy)
    z = slab.positions[:, 2]
    tags = slab.get_tags()
    slab.set_constraint(FixAtoms(mask=(tags < 3)))
    slab.calc = EMT()
    return slab

initial = make_image(fcc_xy)
final = make_image(hcp_xy)

images = [initial] + [initial.copy() for _ in range(3)] + [final]
for img in images[1:-1]:
    img.calc = EMT()
    img.set_constraint(initial.constraints)

neb = NEB(images)
neb.interpolate(method='idpp')

opt = BFGS(neb, logfile=None)
opt.run(fmax=0.05)

energies = np.array([img.get_potential_energy() for img in images])
barrier = energies.max() - energies[0]
print(f'Energy barrier: {barrier:.6f} eV')
