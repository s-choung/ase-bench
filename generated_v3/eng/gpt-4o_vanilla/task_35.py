from ase import Atoms
from ase.calculators.emt import EMT
from ase.neb import NEB
from ase.optimize import BFGS
from ase.build import bulk

# Create initial and final states
initial = Atoms('Al3', positions=[(0, 0, 0), (2, 0, 0), (1, 0.5, 0.5)])
final = Atoms('Al3', positions=[(0, 0, 0), (2, 0, 0), (1, 0, 0)])
initial.set_calculator(EMT())
final.set_calculator(EMT())

# Create interpolated images
images = [initial] + [initial.copy() for _ in range(3)] + [final]
neb = NEB(images)
neb.interpolate()

# Perform NEB calculation
for image in images:
    image.set_calculator(EMT())
neb = NEB(images)
optimizer = BFGS(neb)
optimizer.run(fmax=0.05)

# Print energy of each image
for i, image in enumerate(images):
    print(f'Image {i}: Energy = {image.get_potential_energy():.3f} eV')
