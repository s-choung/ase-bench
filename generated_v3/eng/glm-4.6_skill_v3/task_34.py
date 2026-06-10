from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS
from ase.mep import NEB
import numpy as np

# Create Cu(111) slab
slab = fcc111('Cu', size=(3, 3, 4), vacuum=10.0, a=3.61)
slab.calc = EMT()

# Fix bottom layers
mask = [atom.tag > 1 for atom in slab]
slab.set_constraint(FixAtoms(mask=mask))

# Initial state: Cu adatom at fcc hollow site
initial = slab.copy()
add_adsorbate(initial, 'Cu', height=1.8, position='fcc')

# Final state: Cu adatom at hcp hollow site
final = slab.copy()
add_adsorbate(final, 'Cu', height=1.8, position='hcp')

# Optimize initial and final states
BFGS(initial).run(fmax=0.05, steps=100)
BFGS(final).run(fmax=0.05, steps=100)

# Set up NEB with 5 images (3 intermediate)
images = [initial] + [initial.copy() for _ in range(3)] + [final]
neb = NEB(images)

# IDPP interpolation
neb.interpolate(method='idpp')

# Set calculator for intermediate images
for image in images[1:-1]:
    image.calc = EMT()
    image.set_constraint(FixAtoms(mask=[atom.tag > 1 for atom in image]))

# Run NEB optimization
BFGS(neb).run(fmax=0.05, steps=200)

# Calculate energy barrier
energies = [image.get_potential_energy() for image in images]
barrier = max(energies) - energies[0]
print(f"Energy barrier: {barrier:.3f} eV")
