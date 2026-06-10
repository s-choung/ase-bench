from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.neb import NEB
from ase.optimize import FIRE

# Initial state: two fixed Al atoms at 0 and 5 Å, moving Al at 1 Å
initial = Atoms('Al3', positions=[[0., 0., 0.], [5., 0., 0.], [1., 0., 0.]])
initial.set_calculator(EMT())
initial.set_constraint(FixAtoms(indices=[0, 1]))

# Final state: same fixed atoms, moving Al at 4 Å
final = Atoms('Al3', positions=[[0., 0., 0.], [5., 0., 0.], [4., 0., 0.]])
final.set_calculator(EMT())
final.set_constraint(FixAtoms(indices=[0, 1]))

# Middle image (linear interpolation)
middle = Atoms('Al3', positions=0.5 * (initial.positions + final.positions))
middle.set_calculator(EMT())
middle.set_constraint(FixAtoms(indices=[0, 1]))

# NEB with 3 images
images = [initial, middle, final]
neb = NEB(images, k=0.1)

# Optimize the band
FIRE(neb).run(fmax=0.05, steps=100)

# Print energies of each image
for i, img in enumerate(images):
    print(f'Image {i} energy = {img.get_potential_energy():.4f} eV')
