from ase import Atoms
from ase.calculators.emt import EMT
from ase.neb import NEB
from ase.optimize import BFGS
import numpy as np

# Initial state
initial = Atoms('Al3', positions=[[0, 0, 0], [5, 0, 0], [1, 0, 0]], cell=[10, 10, 10], pbc=False)
initial.calc = EMT()
initial[0].position = [0, 0, 0]
initial[1].position = [5, 0, 0]
initial[2].position = [1, 0, 0]

# Final state
final = initial.copy()
final[2].position = [4, 0, 0]

# Create NEB with 3 images
images = [initial]
for i in range(3):
    image = initial.copy()
    image.positions = initial.positions + (final.positions - initial.positions) * (i + 1) / 4
    images.append(image)
images.append(final)

# Set calculator for all images
for image in images:
    image.calc = EMT()

# Set up NEB
neb = NEB(images)
optimizer = BFGS(neb)
optimizer.run(fmax=0.05, steps=100)

# Print energies
for i, image in enumerate(images):
    print(f"Image {i}: Energy = {image.get_potential_energy():.6f} eV")
