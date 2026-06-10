from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.neb import NEB
from ase.optimize import FIRE

# Initial and final states: two fixed Al atoms at 0,0,0 and 3,0,0
# Third Al atom moves from x=1 to x=2 along x-axis
initial = Atoms('Al3',
                positions=[(0,0,0), (3,0,0), (1,0,0)],
                cell=[10,10,10], pbc=True)
final = Atoms('Al3',
              positions=[(0,0,0), (3,0,0), (2,0,0)],
              cell=[10,10,10], pbc=True)

# Fix the first two atoms
constraint = FixAtoms(indices=[0,1])
initial.set_constraint(constraint.copy())
final.set_constraint(constraint.copy())

# Calculator
calc = EMT()
initial.calc = calc
final.calc = calc

# Create 3 images (including endpoints) using linear interpolation
images = [initial]
for i in range(1, 4):
    image = initial.copy()
    image.calc = calc
    images.append(image)
images.append(final)

neb = NEB(images)
neb.interpolate()

# Optimize the NEB
optimizer = FIRE(neb)
optimizer.run(fmax=0.05)

# Print energies of each image
print("Image energies:")
for i, img in enumerate(images):
    print(f"Image {i}: {img.get_potential_energy():.6f} eV")
