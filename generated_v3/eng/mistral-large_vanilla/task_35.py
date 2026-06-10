from ase import Atoms
from ase.calculators.emt import EMT
from ase.neb import NEB
from ase.optimize import BFGS

# Fixed atoms positions
fixed = Atoms('2Al', positions=[[0, 0, 0], [5, 0, 0]], calculator=EMT())
fixed.set_constraint([0, 1])

# Initial and final states
initial = fixed + Atoms('Al', positions=[[1, 0, 0]], calculator=EMT())
final = fixed + Atoms('Al', positions=[[4, 0, 0]], calculator=EMT())

# NEB setup
images = [initial]
images += [initial.copy() for _ in range(2)]
images += [final]
neb = NEB(images)
neb.interpolate()

# Relaxation
optimizer = BFGS(neb)
optimizer.run(fmax=0.05)

# Print energies
for i, img in enumerate(images):
    print(f"Image {i}: Energy = {img.get_potential_energy():.3f} eV")
