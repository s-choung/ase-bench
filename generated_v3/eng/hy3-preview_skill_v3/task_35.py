from ase import Atoms
from ase.calculators.emt import EMT
from ase.mep import NEB
from ase.optimize import BFGS

# Create initial state: two fixed Al atoms and one moving Al atom
initial = Atoms('Al3', positions=[(0, 0, 0), (8, 0, 0), (2, 0, 0)])
initial.calc = EMT()

# Create final state: moving Al atom has moved to other side
final = initial.copy()
final.positions[2] = (6, 0, 0)
final.calc = EMT()

# Create NEB images with linear interpolation
images = [initial] + [initial.copy() for _ in range(3)] + [final]
neb = NEB(images)
neb.interpolate(method='linear')

# Set calculator for each image
for image in images:
    image.calc = EMT()

# Run NEB optimization
optimizer = BFGS(neb, trajectory='neb.traj')
optimizer.run(fmax=0.05, steps=50)

# Print energy of each image
for i, image in enumerate(images):
    print(f"Image {i}: Energy = {image.get_potential_energy():.4f} eV")
