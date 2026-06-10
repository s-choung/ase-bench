from ase import Atoms
from ase.neb import NEB
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms

initial = Atoms('Al3', positions=[[0, 0, 0], [3.5, 0, 0], [1.75, 0, 0.7]])
final = Atoms('Al3', positions=[[0, 0, 0], [3.5, 0, 0], [1.75, 0, -0.7]])

images = [initial]
images += [initial.copy() for _ in range(3)]
images += [final]

for i, image in enumerate(images[1:-1]):
    image.positions[2] = initial.positions[2] + (final.positions[2] - initial.positions[2]) * (i+1)/4

for image in images:
    image.calc = EMT()
    image.set_constraint(FixAtoms(mask=[True, True, False]))

neb = NEB(images)
neb.interpolate()

for i, image in enumerate(images):
    print(f'Energy of image {i}: {image.get_potential_energy():.3f} eV')
