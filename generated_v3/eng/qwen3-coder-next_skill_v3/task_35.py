from ase import Atoms
from ase.calculators.emt import EMT
from ase.mep import NEB
from ase.optimize import BFGS

# Initial state: Al atom at left, two fixed Al atoms at right
initial = Atoms('Al3', positions=[[0, 0, 0], [2.0, 0, 0], [4.0, 0, 0]])
initial[1].tag = 2  # Fix middle atom (index 1)
initial[2].tag = 2  # Fix right atom (index 2)
initial.calc = EMT()

# Final state: Al atom at right, two fixed Al atoms at left
final = Atoms('Al3', positions=[[0, 0, 0], [2.0, 0, 0], [4.0, 0, 0]])
final[0].tag = 2  # Fix left atom (index 0)
final[1].tag = 2  # Fix middle atom (index 1)
final.calc = EMT()

# Create 3 images (initial + 1 intermediate + final)
images = [initial] + [initial.copy()] + [final]

# Linear interpolation for intermediate image
neb = NEB(images)
neb.interpolate(method='linear')

# Set calculator for all images
for image in images:
    image.calc = EMT()

# Optimize with BFGS
opt = BFGS(neb)
opt.run(fmax=0.05)

# Print energies of all images
for i, image in enumerate(images):
    print(f"Image {i} energy: {image.get_potential_energy():.6f} eV")
