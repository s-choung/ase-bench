from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize.ne import NEB
import numpy as np

# Initial state: two fixed Al atoms
initial = molecule('Al2')
initial.set_constraint(FixAtoms(mask=[0, 1]))
initial.calc = EMT()

# Final state: three Al atoms
final = molecule('Al3')
final.calc = EMT()

# Create images for NEB
images = [initial, initial.copy(), final]

# Perform NEB calculation
neb = NEB(images, shrink=0.1, climb=0.1)
neb.interpolate(method='linear')

# Optimize the images
neb.run(fmax=0.05)

# Print the energy of each image
for i, img in enumerate(images):
    print(f"Image {i+1}: Energy = {img.get_potential_energy():.4f} eV")
