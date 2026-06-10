from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.md import NEB

# Create initial and final states
initial = Atoms('Al3', positions=[[0, 0, 0], [2, 0, 0], [1, 0, 0]])
initial.set_constraint(FixAtoms(indices=[0, 1]))
initial.calc = EMT()

final = Atoms('Al3', positions=[[0, 0, 0], [2, 0, 0], [1.5, 0, 0]])
final.set_constraint(FixAtoms(indices=[0, 1]))
final.calc = EMT()

# Create images with linear interpolation
images = [initial, initial.copy(), final]
for img in images:
    img.calc = EMT()

neb = NEB(images)
neb.interpolate(method='idpp')

# Run optimization
opt = BFGS(neb)
opt.run(fmax=0.05)

# Print energies
for i, img in enumerate(images):
    print(f"Image {i}: Energy = {img.get_potential_energy()} eV")
