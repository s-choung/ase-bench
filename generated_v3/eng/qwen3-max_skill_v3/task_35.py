from ase import Atoms
from ase.calculators.emt import EMT
from ase.mep import NEB
from ase.optimize import BFGS

# Create initial state: Al atom at (0,0,0), fixed Al atoms at (-2,0,0) and (2,0,0)
initial = Atoms('Al3', positions=[(-2, 0, 0), (0, 0, 0), (2, 0, 0)])
initial.calc = EMT()

# Create final state: Al atom at (0,0,0) moved to (0,0,2)
final = Atoms('Al3', positions=[(-2, 0, 0), (0, 0, 2), (2, 0, 0)])
final.calc = EMT()

# Fix terminal atoms in both end points
initial.set_constraint([0, 2])
final.set_constraint([0, 2])

# Optimize initial and final states
BFGS(initial).run(fmax=0.01)
BFGS(final).run(fmax=0.01)

# Create 3 images (including endpoints) -> 1 intermediate image
images = [initial]
images.append(initial.copy())
images.append(final)

# Set up NEB
neb = NEB(images)
neb.interpolate()  # linear interpolation

# Set calculators for intermediate images
for image in images[1:-1]:
    image.calc = EMT()

# Optimize NEB
BFGS(neb).run(fmax=0.05)

# Print energies
for i, image in enumerate(images):
    print(f"Image {i}: energy = {image.get_potential_energy():.6f} eV")
