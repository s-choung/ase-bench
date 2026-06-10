from ase import Atoms
from ase.calculators.emt import EMT
from ase.neb import NEB
from ase.optimize import FIRE

# Create initial state: two fixed Al atoms and one moving
initial = Atoms('Al3', positions=[[0, 0, 0], [6, 0, 0], [2, 0, 0]], cell=[10, 5, 5], pbc=False)
initial.calc = EMT()

# Create final state: moving atom on opposite side
final = Atoms('Al3', positions=[[0, 0, 0], [6, 0, 0], [4, 0, 0]], cell=[10, 5, 5], pbc=False)
final.calc = EMT()

# Fix first two atoms in both states
from ase.constraints import FixAtoms
constraint = FixAtoms(indices=[0, 1])
initial.set_constraint(constraint)
final.set_constraint(constraint)

# Create 3 images with linear interpolation
images = [initial]
for i in range(1, 3):
    image = initial.copy()
    image.calc = EMT()
    image.set_constraint(constraint)
    images.append(image)
images.append(final)

# Set up NEB
neb = NEB(images)
neb.interpolate()

# Run quick optimization
optimizer = FIRE(neb, trajectory='neb.traj')
optimizer.run(fmax=0.1, steps=10)

# Print energies
for i, image in enumerate(images):
    print(f"Image {i}: Energy = {image.get_potential_energy():.4f} eV")
