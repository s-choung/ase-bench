from ase import Atoms
from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.mep import NEB
from ase.optimize import BFGS
import numpy as np

# Build Cu FCC(111) slab
slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0)
slab.calc = EMT()

# Fix bottom two layers
mask = [atom.tag <= 2 for atom in slab]
slab.set_constraint(FixAtoms(mask=mask))

# Initial state: Cu adatom at fcc hollow site
initial = slab.copy()
add_adsorbate(initial, Atoms('Cu'), height=1.5, position='hollow')

# Final state: Cu adatom at hcp hollow site
final = slab.copy()
add_adsorbate(final, Atoms('Cu'), height=1.5, position='hollow')
# Shift adatom to adjacent hcp site (approximate translation)
final.positions[-1] += np.array([initial.cell[0, 0]/2, initial.cell[1, 1]/2, 0])

# Create NEB images
images = [initial.copy() for _ in range(5)]
images[0] = initial
images[-1] = final

# Set calculator for each image
for image in images:
    image.calc = EMT()

# Run NEB with IDPP interpolation
neb = NEB(images)
neb.interpolate(method='idpp')

# Optimize NEB
optimizer = BFGS(neb, trajectory='neb.traj')
optimizer.run(fmax=0.05)

# Find energy barrier
energies = [img.get_potential_energy() for img in images]
barrier = max(energies) - energies[0]
print(f"Energy barrier: {barrier:.3f} eV")
