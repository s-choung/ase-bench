from ase import Atoms
from ase.calculators.emt import EMT
from ase.neb import NEB
from ase.optimize import FIRE

# Create initial state: Al-Al-Al in a line with Al1 fixed, Al3 fixed, Al2 moving
initial = Atoms('Al3', positions=[(0, 0, 0), (2.0, 0, 0), (4.0, 0, 0)])
initial.set_constraint([0, 1, 2])  # Fix all atoms initially

# Create final state: Al3 moves closer to Al1
final = Atoms('Al3', positions=[(0, 0, 0), (1.0, 0, 0), (4.0, 0, 0)])
final.set_constraint([0, 1, 2])

# Set calculator
calc = EMT()
initial.calc = calc
final.calc = calc

# Create NEB with 3 images (including endpoints)
images = [initial]
images += [initial.copy() for _ in range(1)]
images.append(final)
neb = NEB(images, climb=False)

# Interpolate linearly between initial and final
neb.interpolate()

# Fix atoms 0 and 2 in all images (Al1 and Al3)
for image in images:
    image.set_constraint([0, 2])

# Set calculator for all images
for image in images:
    image.calc = calc

# Optimize
optimizer = FIRE(neb)
optimizer.run(fmax=0.05)

# Print energies
for i, image in enumerate(images):
    print(f'Image {i}: energy = {image.get_potential_energy():.6f} eV')
