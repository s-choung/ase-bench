from ase import Atoms
from ase.calculators.emt import EMT
from ase.neb import NEB
from ase.optimize import BFGS
import numpy as np

# Initial state: third Al atom on the left side
initial = Atoms('Al3', positions=[
    [0.0, 0.0, 0.0],
    [4.0, 0.0, 0.0],
    [1.0, 1.5, 0.0]
])
initial.calc = EMT()

# Final state: third Al atom on the right side
final = Atoms('Al3', positions=[
    [0.0, 0.0, 0.0],
    [4.0, 0.0, 0.0],
    [3.0, 1.5, 0.0]
])
final.calc = EMT()

# Create 3 images (initial + 1 intermediate + final)
n_images = 3
images = [initial]
for i in range(n_images - 2):
    image = initial.copy()
    image.calc = EMT()
    images.append(image)
images.append(final)

# NEB with linear interpolation
neb = NEB(images)
neb.interpolate()

# Optimize NEB
optimizer = BFGS(neb, logfile=None)
optimizer.run(fmax=0.05, steps=200)

# Print energies
print("Image energies after NEB optimization:")
print(f"{'Image':>6} {'Energy (eV)':>14}")
print("-" * 22)
for i, image in enumerate(images):
    energy = image.get_potential_energy()
    label = "initial" if i == 0 else ("final" if i == len(images)-1 else f"TS-{i}")
    print(f"{i:>6} {energy:>14.6f}  ({label})")

# Print barrier
energies = [img.get_potential_energy() for img in images]
e_initial = energies[0]
e_max = max(energies)
barrier = e_max - e_initial
print(f"\nInitial energy : {e_initial:.6f} eV")
print(f"Max energy     : {e_max:.6f} eV")
print(f"Energy barrier : {barrier:.6f} eV")
