from ase.build import surface
from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS
from ase.mep import NEB
import numpy as np

# Build Cu(111) slab
slab = surface('Cu', (1, 1, 1), size=(2, 2, 4), vacuum=10.0)
tags = slab.get_tags()

# Determine hollow sites from ideal stacking
top_atoms = slab[tags == 0]
second_atoms = slab[tags == 1]
third_atoms = slab[tags == 2]

z_top = np.mean(top_atoms.positions[:, 2])
h_ads = 2.0  # initial height guess

# fcc hollow: above a third-layer atom; hcp hollow: above a second-layer atom
fcc_xy = third_atoms.positions[0, :2].copy()
hcp_xy = second_atoms.positions[0, :2].copy()

def add_adatom(slab, xy, height):
    """Return slab with Cu adatom placed at (xy, height)."""
    slab_copy = slab.copy()
    slab_copy += Atoms('Cu', positions=[(xy[0], xy[1], height)])
    return slab_copy

# Create endpoints
initial = add_adatom(slab, fcc_xy, z_top + h_ads)
final = add_adatom(slab, hcp_xy, z_top + h_ads)

# Fix bottom layers (tags >= 2) during relaxation
mask = [tag >= 2 for tag in initial.get_tags()]
fix = FixAtoms(mask=mask)
for atoms in [initial, final]:
    atoms.set_constraint(fix)
    atoms.calc = EMT()
    BFGS(atoms, logfile=None).run(fmax=0.05)

# NEB with 5 intermediate images and IDPP interpolation
n_images = 5
images = [initial]
images += [initial.copy() for _ in range(n_images)]
images += [final]

neb = NEB(images, remove_rotation_and_translation=False)
neb.interpolate(method='idpp')

for img in images[1:-1]:
    img.calc = EMT()
# final already has a calculator

opt = BFGS(neb, logfile=None)
opt.run(fmax=0.05)

# Energy barrier
energies = np.array([img.get_potential_energy() for img in images])
barrier = np.max(energies) - energies[0]
print(f"Energy barrier: {barrier:.3f} eV")
