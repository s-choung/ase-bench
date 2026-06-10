from ase.neb import NEB
from ase.optimize import MDMin
from ase.calculators.emt import EMT
from ase.atoms import Atoms

# Initial state: two Al atoms at equilibrium distance
initial = Atoms('Al2', positions=[[0, 0, 0], [2.82, 0, 0]], calculator=EMT())

# Final state: two Al atoms with third Al atom close to the second one
final = Atoms('Al3', positions=[[0, 0, 0], [2.82, 0, 0], [3.5, 0, 0]], calculator=EMT())

# Create NEB object with 3 images and linear interpolation
neb = NEB([initial, final], interpolate='idpp', fmax=0.05)

# Set EMT calculator for all images
for atoms in neb.images:
    atoms.set_calculator(EMT())

# Optimize NEB path
optimizer = MDMin(neb, trajectory=None)
optimizer.run(steps=100)

# Print energy of each image
for i, image in enumerate(neb.images):
    print(f'Image {i+1}: Energy = {image.get_potential_energy():.4f} eV')
