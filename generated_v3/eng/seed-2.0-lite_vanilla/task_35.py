from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.neb import NEB
from ase.optimize import BFGS

# Create initial and final states
initial = Atoms('Al3', positions=[[0, 0, 0], [6, 0, 0], [2, 0, 0]], cell=[10,10,10], pbc=False)
final = Atoms('Al3', positions=[[0, 0, 0], [6, 0, 0], [4, 0, 0]], cell=[10,10,10], pbc=False)

# Create list of 3 images (initial, intermediate, final)
images = [initial.copy() for _ in range(3)]
images[-1] = final.copy()

# Linear interpolation of positions between end states
neb = NEB(images)
neb.interpolate()

# Assign calculator and fix the two end Al atoms for all images
for image in images:
    image.set_calculator(EMT())
    image.set_constraint(FixAtoms(indices=[0, 1]))

# Set up and run NEB relaxation
neb = NEB(images, k=0.1)
opt = BFGS(neb, logfile=None)
opt.run(fmax=0.01)

# Print energies of all images
for idx, img in enumerate(images):
    print(f"Image {idx}: Energy = {img.get_potential_energy():.4f} eV")
