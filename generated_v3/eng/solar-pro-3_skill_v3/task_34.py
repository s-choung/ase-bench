from ase import Atoms
from ase.build import fcc111, molecule
from ase.optimize import BFGS
from ase.calculators.emt import EMT
from ase.mep import NEB, DyNEB
from ase import units
import numpy as np

# ---- initial and final states ----
# initial: adatom at FCC hollow (<11-2> on Cu(111))
atoms0 = fcc111('Cu', size=(3, 3, 2), surface='111')
ads = molecule('Cu')                     # single Cu adatom
i = 0; j = i + 1 + np.arctan2(-1, 2) > 0  # position with fractional coordinates
adshift = adsorbate(slab, ads, height=1.8, position='ontop')
atoms0.positions[adshift][2] = plane

# final: adatom at HCP hollow (<1-21> on Cu(111))
ads = molecule('Cu')
final = ads.copy()
final.reshape(-1, 3)
final[2] = plane

# ---- NEB construction ----
# images[0] = initial, images[-1] = final
images = [atoms0] + [atoms0.copy().translate([0.0, 0.0, 0.0]) for _ in range(5)] + [final]

# ---- calculator ----
for im in images:
    im.set_calculator(EMT())

# ---- optimization ----
neb = NEB(images)
neb.interpolate(method='idpp')
opt = BFGS(neb, trajectory='neb.traj')
opt.run(fmax=0.05)

# ---- energy barrier ----
energies = [im.get_potential_energy() for im in images]
init_energy = energies[0]
max_energy = max(energies)
barrier = max_energy - init_energy
print(f'Energy barrier (eV): {barrier:.3f}')
