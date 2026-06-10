from ase.build import bulk
from ase.calculators.emt import EMT
from ase.mep import NEB, NEBTools
from ase.optimize import BFGS
import numpy as np

al = bulk("Al", "fcc", a=4.05, cubic=True).repeat((3, 3, 3))

center = al.cell.lengths() / 2
vac_idx = np.argmin(np.linalg.norm(al.positions - center, axis=1))
vac_pos = al.positions[vac_idx].copy()

d = al.get_distances(vac_idx, range(len(al)), mic=True)
d[vac_idx] = np.inf
nbr_idx = np.argmin(d)

initial = al.copy()
del initial[vac_idx]

move_idx = nbr_idx - 1 if nbr_idx > vac_idx else nbr_idx
final = initial.copy()
final.positions[move_idx] = vac_pos

images = [initial]
images += [initial.copy() for _ in range(3)]
images += [final]

for img in images:
    img.calc = EMT()

neb = NEB(images, climb=True)
neb.interpolate(mic=True)

opt = BFGS(neb, logfile="neb.log", trajectory="neb.traj")
opt.run(fmax=0.05)

nebtools = NEBTools(images)
barrier, dE = nebtools.get_barrier(fit=True)

print(f"Barrier height: {barrier:.6f} eV")
print(f"Reaction energy: {dE:.6f} eV")
