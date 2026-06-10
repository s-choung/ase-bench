from ase import Atoms
from ase.calculators.emt import EMT
from ase.mep import NEB
from ase.optimize import BFGS
import numpy as np

# Initial state: Al atom at (-2, 0, 0)
initial = Atoms('Al3', positions=[[-2, 0, 0], [0, 0, 0], [2, 0, 0]])
initial.set_constraint([0, 2])  # Fix first and last atoms
initial.calc = EMT()

# Final state: Al atom at (2, 0, 0)
final = Atoms('Al3', positions=[[-2, 0, 0], [2, 0, 0], [2, 0, 0]])
final.set_constraint([0, 2])    # Fix first and last atoms
final.calc = EMT()

# Create NEB images
images = [initial] + [initial.copy() for _ in range(3)] + [final]
neb = NEB(images)
neb.interpolate()

# Set calculator for images
for img in images[1:-1]:
    img.calc = EMT()

# Optimize NEB path
optimizer = BFGS(neb)
optimizer.run(fmax=0.05)

# Print energies of images
for i, img in enumerate(images):
    print(f'Image {i}: {img.get_potential_energy():.4f} eV')
