from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.mep import NEB

# Initial state: Al--Al--Al (mobile atom on left)
initial = Atoms('Al3', positions=[[0, 0, 0], [1, 0, 0], [3, 0, 0]])
initial.calc = EMT()

# Final state: Al--Al--Al (mobile atom on right)
final = Atoms('Al3', positions=[[0, 0, 0], [2, 0, 0], [3, 0, 0]])
final.calc = EMT()

# Create 3 images (initial, 1 intermediate, final)
images = [initial] + [initial.copy() for _ in range(1)] + [final]

# Set up NEB with linear interpolation
neb = NEB(images)
neb.interpolate()

# Set calculator for intermediate images
for img in images[1:-1]:
    img.calc = EMT()

# Optimize NEB
BFGS(neb).run(fmax=0.05, steps=100)

# Print energies
for i, img in enumerate(images):
    print(f"Image {i}: Energy = {img.get_potential_energy():.6f} eV")
