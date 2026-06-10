from ase import Atoms
from ase.calculators.emt import EMT
from ase.neb import NEB
from ase.optimize import BFGS

# Create initial and final states
initial = Atoms('Al3', positions=[[0.0, 0.0, 0.0],
                                  [2.0, 0.0, 0.0],
                                  [4.0, 0.0, 0.0]])
final = Atoms('Al3', positions=[[0.0, 0.0, 0.0],
                                [2.0, 0.0, 0.0],
                                [0.0, 0.0, 0.0]])

# Fix the first two atoms
initial.set_constraint([0, 1])
final.set_constraint([0, 1])

# Set calculator
calc = EMT()
initial.calc = calc
final.calc = calc

# Create images
images = [initial]
images += [initial.copy() for _ in range(3)]
images.append(final)

# Interpolate and set constraints
neb = NEB(images)
neb.interpolate()
for image in images[1:-1]:
    image.set_constraint([0, 1])
    image.calc = calc

# Optimize
opt = BFGS(neb)
opt.run(fmax=0.05)

# Print energies
for i, image in enumerate(images):
    print(f"Image {i}: {image.get_potential_energy():.6f} eV")
