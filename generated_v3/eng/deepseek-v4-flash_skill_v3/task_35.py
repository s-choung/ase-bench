from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.mep import NEB
from ase.constraints import FixAtoms
import numpy as np

# Define positions: two fixed Al atoms at 0 and 4 Å, moving Al in between
p0 = [0.0, 0.0, 0.0]
p1 = [4.0, 0.0, 0.0]
pi = [1.0, 0.0, 0.0]
pf = [3.0, 0.0, 0.0]

# Initial and final structures
initial = Atoms('Al3', positions=[p0, p1, pi])
final = initial.copy()
final.positions[2] = pf

# Fix the two end atoms
constraint = FixAtoms(indices=[0, 1])
initial.set_constraint(constraint)
final.set_constraint(constraint)

# Set calculators
calc = EMT()
initial.calc = calc
final.calc = calc

# Create NEB with 3 intermediate images
n_images = 3
images = [initial] + [initial.copy() for _ in range(n_images)] + [final]
for img in images:
    img.calc = EMT()

# Set up NEB and interpolate
neb = NEB(images)
neb.interpolate(method='linear')

# Optimize
opt = BFGS(neb)
opt.run(fmax=0.05)

# Print energies
for i, img in enumerate(images):
    print(f'Image {i}: {img.get_potential_energy():.4f} eV')
