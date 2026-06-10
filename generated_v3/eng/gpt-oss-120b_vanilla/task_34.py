import numpy as np
from ase import Atoms
from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.neb import NEB, IDPPInterpolator
from ase.optimize import BFGS

# ---- Build Cu(111) slab ----
slab = fcc111('Cu', size=(3, 3, 3), vacuum=10.0, periodic=True)
slab.center(vacuum=10.0, axis=2)

# ---- Define fcc and hcp hollow positions ----
a = slab.get_cell_lengths_and_angles()[0]
# fractional positions in the surface unit cell
fcc_frac = np.array([1/3, 2/3, 0.5])
hcp_frac = np.array([2/3, 1/3, 0.5])
# Convert to cartesian and raise adatom ~1.8 Å above surface
height = 1.8
fcc_pos = np.dot(fcc_frac[:2], slab.get_cell()[:2, :2])
hcp_pos = np.dot(hcp_frac[:2], slab.get_cell()[:2, :2])
fcc_pos = np.append(fcc_pos, slab.positions[:, 2].max() + height)
hcp_pos = np.append(hcp_pos, slab.positions[:, 2].max() + height)

# ---- Create initial and final configurations ----
initial = slab.copy()
add_adsorbate(initial, 'Cu', height, position=fcc_frac[:2])
initial[-1].position = fcc_pos

final = slab.copy()
add_adsorbate(final, 'Cu', height, position=hcp_frac[:2])
final[-1].position = hcp_pos

# ---- Prepare images for NEB (5 total: 2 endpoints + 3 interpolated) ----
images = [initial]
for _ in range(3):
    images.append(initial.copy())
images.append(final)

calc = EMT()
for img in images:
    img.set_calculator(calc)

# ---- IDPP interpolation ----
IDPPInterpolator(images).interpolate()

# ---- NEB with climbing image ----
neb = NEB(images, climb=True)
opt = BFGS(neb, logfile='neb.log')
opt.run(fmax=0.05)

# ---- Energy barrier ----
energies = [img.get_potential_energy() for img in images]
E0 = energies[0]
Emax = max(energies)
barrier = Emax - E0
print(f'Energy barrier = {barrier:.3f} eV')
