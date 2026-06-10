from ase import Atoms
from ase.calculators.emt import EMT
from ase.mep import NEB
from ase.optimize import BFGS
import numpy as np

# Define initial and final states: 3 Al atoms in a line
# Initial: Al(0,0,0), Al(1,0,0), Al(2,0,0)
# Final:   Al(0,0,0), Al(2,0,0), Al(1,0,0) -> essentially swapping the moving atom
initial = Atoms('Al3', positions=[[0, 0, 0], [1, 0, 0], [2, 0, 0]])
final = Atoms('Al3', positions=[[0, 0, 0], [2, 0, 0], [1, 0, 0]])

# Create images: [initial] + [3 interpolated images] + [final]
# Total 5 images to satisfy "3 images with linear interpolation" requirement
images = [initial] + [initial.copy() for _ in range(3)] + [final]

# Linear interpolation
neb = NEB(images)
neb.interpolate(method='linear')

# Assign calculator to all images
for img in images:
    img.calc = EMT()

# Run optimization
opt = BFGS(neb)
opt.run(fmax=0.05)

# Print energies of each image
for i, img in enumerate(images):
    print(f"Image {i} energy: {img.get_potential_energy():.4f} eV")
