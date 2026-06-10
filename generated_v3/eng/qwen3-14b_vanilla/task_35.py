from ase import Atoms
from ase.neb import NEB
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms

# Create initial and final states
initial = Atoms('Al3', positions=[[0,0,0], [3.0,0,0], [0.5,0,0]])
final = Atoms('Al3', positions=[[0,0,0], [3.0,0,0], [2.5,0,0]])

# Fix first two atoms
constraint = FixAtoms(mask=[True, True, False])
initial.set_constraint(constraint)
final.set_constraint(constraint)

# Generate 3 images with interpolation
images = [initial, final]
neb = NEB(images)
neb.interpolate(images=3)

# Set EMT calculator
for img in images:
    img.set_calculator(EMT())

# Print energy of each image
for i, img in enumerate(images):
    print(f"Image {i}: {img.get_potential_energy()} eV")
