from ase import Atoms
from ase.build import make_supercell
from ase.calculators.emt import EMT
from ase.io import write
from ase.optimize import BFGS
from ase.constraints import FixAtoms
from ase.neb import NEB

# Define initial and final states
initial = Atoms('Al', positions=[(0, 0, 0), (2, 0, 0), (4, 0, 0)],
                 cell=(6, 1, 1), pbc=(True, False, False))
final = Atoms('Al', positions=[(0, 0, 0), (2, 0, 0), (6, 0, 0)],
               cell=(8, 1, 1), pbc=(True, False, False))

# Create 3 images (including initial and final states)
images = [initial.copy() for _ in range(3)]
images[-1] = final.copy()

# Set EMT calculator for each image
for image in images:
    image.calc = EMT()

# Use linear interpolation
neb = NEB(images)
neb.interpolate()

# Fix the first and last Al atoms
neb[0].set_constraint(FixAtoms(mask=[1, 1, 0]))
neb[-1].set_constraint(FixAtoms(mask=[1, 1, 0]))

# Optimize the NEB path
optimizer = BFGS(neb, trajectory='neb.traj')
optimizer.run(fmax=0.05)

# Print the energy of each image
for i, image in enumerate(images):
    energy = image.get_potential_energy()
    print(f"Image {i+1} energy: {energy} eV")
