from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.neb import NEB
from ase import Atoms

# Define initial and final states
initial = Atoms('Al', positions=[(0, 0, 0), (2, 0, 0), (4, 0, 0)], cell=[10, 10, 10], pbc=False)
final = Atoms('Al', positions=[(0, 0, 0), (2, 0, 0), (8, 0, 0)], cell=[10, 10, 10], pbc=False)

# Create intermediate states for linear interpolation
images = [initial.copy()] + [[initial_i.flip_z()] for initial_i in [initial, final]]

# Set up NEB calculation
neb = NEB(images)
neb.interpolate(method='linear')

# Set EMT calculator
for img in images:
    img.calc = EMT()

# Optimize NEB
opt = BFGS(neb)
opt.run(fmax=0.05)

# Print energy of each image
for i, img in enumerate(images):
    print(f"Image {i}: Energy = {img.get_potential_energy():.6f} eV")
