from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.mep import NEB

# Define initial state
initial = Atoms('Al3', positions=[(0, 0, 0), (0, 0, 3), (0, 0, 1)])
initial.calc = EMT()

# Define final state
final = Atoms('Al3', positions=[(0, 0, 0), (0, 0, 3), (0, 0, 2)])
final.calc = EMT()

# Create NEB images
images = [initial]
for i in range(3):
    image = initial.copy()
    image.calc = EMT()
    images.append(image)
images.append(final)

# Set up NEB
neb = NEB(images)
neb.interpolate()

# Run NEB optimization
optimizer = BFGS(neb)
optimizer.run(fmax=0.05)

# Print energies of each image
for i, image in enumerate(images):
    print(f"Image {i}: Energy = {image.get_potential_energy()} eV")
