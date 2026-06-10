from ase import Atoms
from ase.calculators.emt import EMT
from ase.neb import NEB
from ase.optimize import BFGS

# Initial state: Al atom at (0,0,0)
initial = Atoms('Al3', positions=[(0, 0, 0), (2, 0, 0), (0, 0, 0)])
initial.set_calculator(EMT())

# Final state: Al atom at (2,0,0)
final = Atoms('Al3', positions=[(0, 0, 0), (2, 0, 0), (2, 0, 0)])
final.set_calculator(EMT())

# 3 images including endpoints (1 intermediate)
images = [initial.copy() for i in range(3)]
for image in images:
    image.set_calculator(EMT())

# Linear interpolation of positions
neb = NEB(images)
neb.interpolate()

# Optimization
optimizer = BFGS(neb)
optimizer.run(fmax=0.05)

# Print energies
for i, image in enumerate(images):
    print(f"Image {i} energy: {image.get_potential_energy():.4f} eV")
