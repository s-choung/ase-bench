from ase import Atoms
from ase.calculators.emt import EMT
from ase.mep import NEB
from ase.optimize import BFGS

# Fixed Al-Al distance
d = 5.0

# Initial state: Al3 between Al1 and Al2 (left)
initial = Atoms('Al3', positions=[[0, 0, 0], [d, 0, 0], [d/3, 0, 0]])
initial.set_calculator(EMT())

# Final state: Al3 between Al1 and Al2 (right)
final = Atoms('Al3', positions=[[0, 0, 0], [d, 0, 0], [2*d/3, 0, 0]])
final.set_calculator(EMT())

# NEB images
images = [initial] + [initial.copy() for _ in range(3)] + [final]
neb = NEB(images)
neb.interpolate(method='linear')

# Relax
for img in images[1:-1]:
    img.set_calculator(EMT())

opt = BFGS(neb)
opt.run(fmax=0.05)

# Print energies
for i, img in enumerate(images):
    print(f"Image {i}: {img.get_potential_energy():.3f} eV")
