import numpy as np
from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.neb import NEB, IDPP
from ase.optimize import BFGS

# Build Cu(111) surface
slab = fcc111('Cu', size=(5, 5, 4), vacuum=10.0, periodic=True)
calc = EMT()

# Initial position (fcc hollow site)
initial = slab.copy()
add_adsorbate(initial, 'Cu', 2.0, 'fcc')

# Final position (hcp hollow site)
final = slab.copy()
add_adsorbate(final, 'Cu', 2.0, 'hcp')

# Optimize initial and final states
for img in [initial, final]:
    img.calc = calc
    BFGS(img, logfile=None).run(fmax=0.05)

# Create NEB images
images = [initial.copy() for _ in range(5)]
images[-1] = final.copy()

# Set calculator for all images
for img in images:
    img.calc = calc

# IDPP interpolation
idpp = IDPP(images)
idpp.interpolate()

# Run NEB optimization
neb = NEB(images, method='ci-neb')
BFGS(neb, logfile=None).run(fmax=0.05)

# Calculate energy barrier
energies = [img.get_potential_energy() for img in images]
barrier = max(energies) - energies[0]
print(f"Energy barrier: {barrier:.4f} eV")
