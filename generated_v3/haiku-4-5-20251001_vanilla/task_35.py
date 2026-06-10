from ase import Atoms
from ase.calculators.emt import EMT
from ase.neb import NEB
from ase.optimize import BFGS
from ase.io import read, write

# Initial state: Al atom between two Al atoms (left side)
initial = Atoms('Al3', positions=[[0, 0, 0], [2.5, 0, 0], [1.2, 0, 0]])
initial.set_calculator(EMT())

# Final state: Al atom between two Al atoms (right side)
final = Atoms('Al3', positions=[[0, 0, 0], [2.5, 0, 0], [1.8, 0, 0]])
final.set_calculator(EMT())

# Create NEB with 3 images (initial + 1 intermediate + final)
images = [initial]
for i in range(1):
    images.append(initial.copy())
images.append(final)

# Linear interpolation
neb = NEB(images)
neb.interpolate()

# Set calculators for all images
for image in images:
    image.set_calculator(EMT())

# Optimize
dyn = BFGS(neb, trajectory='neb.traj')
dyn.run(fmax=0.05, steps=100)

# Print energies
print("NEB Results:")
for i, image in enumerate(images):
    print(f"Image {i}: E = {image.get_potential_energy():.6f} eV")
