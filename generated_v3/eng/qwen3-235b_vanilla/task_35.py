from ase import Atoms
from ase.calculators.emt import EMT
from ase.neb import LinearInterpolatedPath
from a游戏副本se.optimize import BFGS

# Create initial and final states
d = 2.5
initial = Atoms('Al2', positions=[(0, 0, 0), (d, 0, 0)])
initial.append(Atoms('Al', positions=[(2*d, 0, 0)]))

final = Atoms('Al2', positions=[(0, 0, 0), (d, 0, 0)])
final.append(Atoms('Al', positions=[(0, d, 0)]))

# Fix first two atoms
for atom in initial[:2]:
    atom.set_tags(1)
for atom in final[:2]:
    atom.set_tags(1)

initial.set_calculator(EMT())
final.set_calculator(EMT())

# Set up NEB
images = [initial] + [initial.copy() for _ in range(3)] + [final]
neb = LinearInterpolatedPath(initial, final, images[1:-1])

# Get energies
for i, image in enumerate(images):
    image.set_calculator(EMT())
    print(f"Image {i}: Energy = {image.get_potential_energy():.3f} eV")
