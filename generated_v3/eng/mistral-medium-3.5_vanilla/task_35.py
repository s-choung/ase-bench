from ase import Atoms
from ase.calculators.emt import EMT
from ase.neb import NEB
from ase.io import write

# Initial state: Al atom near first fixed Al
initial = Atoms('Al3', positions=[[0, 0, 0], [5, 0, 0], [1, 0, 0]])
initial.calc = EMT()

# Final state: Al atom near second fixed Al
final = Atoms('Al3', positions=[[0, 0, 0], [5, 0, 0], [4, 0, 0]])
final.calc = EMT()

# Create NEB with 3 images
 images = [initial] + [initial.copy() for _ in range(1)] + [final]
 neb = NEB(images, k=0.1)
 neb.interpolate()

# Calculate energies
 for i, image in enumerate(images):
     image.calc = EMT()
     e = image.get_potential_energy()
     print(f'Image {i}: Energy = {e:.4f} eV')
