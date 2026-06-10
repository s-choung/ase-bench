import numpy as np
from ase import Atoms
from ase.calculators.emt import EMT
from ase.mep import NEB
from ase.optimize import BFGS

# Two fixed Al atoms at (0,0,0), (4,0,0), third atom moves between them
pos_init = np.array([[0,0,0],[4,0,0],[1,0,0]])  # third atom near atom 1
pos_final = np.array([[0,0,0],[4,0,0],[3,0,0]]) # third atom near atom 2

initial = Atoms('Al3', positions=pos_init)
final = Atoms('Al3', positions=pos_final)
for atoms in (initial, final):
    atoms.calc = EMT()

# 3 images (initial, 1 intermediate, final)
images = [initial]
for _ in range(1):
    images.append(initial.copy())
images.append(final)

neb = NEB(images)
neb.interpolate(method='linear')
for img in images[1:-1]:
    img.calc = EMT()

optimizer = BFGS(neb)
optimizer.run(fmax=0.05)

for i, img in enumerate(images):
    e = img.get_potential_energy()
    print(f'Image {i}: Energy = {e:.6f} eV')
