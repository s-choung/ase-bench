from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS
from ase.mep import NEB, IDPP
from ase.geometry import get_distances
from copy import deepcopy
import numpy as np

a = 3.61
slab = fcc111('Cu', size=(2, 2, 4), a=a, vacuum=8.0)
z = slab.positions[:, 2]
fix = FixAtoms(mask=z < np.sort(np.unique(np.round(z, 6)))[-2])
slab.set_constraint(fix)

xy = slab.positions[:, :2]
zmax = slab.positions[:, 2].max()
top = np.where(np.abs(slab.positions[:, 2] - zmax) < 1e-3)[0]

def hollow_sites(top_xy):
    pts = []
    n = len(top_xy)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                c = (top_xy[i] + top_xy[j] + top_xy[k]) / 3.0
                d = np.linalg.norm(top_xy - c, axis=1)
                if np.all(d > 0.3):
                    pts.append(c)
    uniq = []
    for p in pts:
        if not any(np.linalg.norm(p - q) < 1e-3 for q in uniq):
            uniq.append(p)
    return np.array(uniq)

sites = hollow_sites(xy[top])
center = xy.mean(axis=0)
sites = sorted(sites, key=lambda p: np.linalg.norm(p - center))
fcc_xy, hcp_xy = sites[:2]

h = 1.8

initial = slab.copy()
add_adsorbate(initial, 'Cu', h, position=fcc_xy)
initial.calc = EMT()
BFGS(initial, logfile=None).run(fmax=0.05)

final = slab.copy()
add_adsorbate(final, 'Cu', h, position=hcp_xy)
final.calc = EMT()
BFGS(final, logfile=None).run(fmax=0.05)

images = [initial]
for _ in range(3):
    img = initial.copy()
    img.calc = EMT()
    images.append(img)
images.append(final)

neb = NEB(images)
neb.interpolate()
idpp = IDPP(images)
BFGS(idpp, logfile=None).run(fmax=0.05)

for img in images:
    img.calc = EMT()

neb = NEB(images)
BFGS(neb, logfile=None).run(fmax=0.05)

energies = [img.get_potential_energy() for img in images]
barrier = max(energies) - energies[0]
print(f'Energy barrier: {barrier:.6f} eV')
