from ase import Atoms
from ase.calculators.emt import EMT
from ase.neb import NEB
from ase.optimize import BFGS

# Create initial state: Al atom at (0, 0, 0) and (2, 0, 0), with third atom at (-1, 0, 0)
initial = Atoms('Al3',
                positions=[[-1.0, 0.0, 0.0],
                           [0.0, 0.0, 0.0],
                           [2.0, 0.0, 0.0]],
                calculator=EMT())

# Create final state: same as initial but with the third atom moved to (3, 0, 0)
final = Atoms('Al3',
              positions=[[0.0, 0.0, 0.0],
                         [2.0, 0.0, 0.0],
                         [3.0, 0.0, 0.0]],
              calculator=EMT())

# Set fixed atoms (first two atoms)
constraints = [constraint for constraint in [range(2)]]
for atoms in [initial, final]:
    atoms.set_constraint(constraints)

# Create 3 images (including initial and final)
images = [initial]
images.append(initial.copy())
images.append(final)

# Interpolate positions for middle image
neb = NEB(images)
neb.interpolate()

# Optimize each image individually
for i, image in enumerate(images):
    image.calc = EMT()
    opt = BFGS(image)
    opt.run(fmax=0.05)

# Print energies of each image
for i, image in enumerate(images):
    print(f"Image {i}: Energy = {image.get_potential_energy():.6f} eV")
