from ase import Atoms
from ase.calculators.emt import EMT
from ase.mep import NEB
from ase.optimize import BFGS

# Initial state: Al atom at (0,0,0)
initial = Atoms('Al3', positions=[(0, 0, 0), (4, 0, 0), (1, 0, 0)])
initial.calc = EMT()

# Final state: Al atom at (3,0,0)
final = Atoms('Al3', positions=[(0, 0, 0), (4, 0, 0), (3, 0, 0)])
final.calc = EMT()

# Create 3 images total (1 intermediate image)
images = [initial] + [initial.copy() for _ in range(1)] + [final]

# Setup NEB and interpolate
neb = NEB(images)
neb.interpolate()

# Set calculators for all images
for img in images:
    img.calc = EMT()

# Optimize the intermediate image
opt = BFGS(neb)
opt.run(fmax=0.05)

# Print energies
for i, img in enumerate(images):
    print(f"Image {i} energy: {img.get_potential_energy():.4f} eV")
