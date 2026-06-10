from ase import Atoms
from ase.calculators.emt import EMT
from ase.neb import NEB
from ase.optimize import BFGS

# fixed atoms and moving atom positions
fixed1 = [0, 0, 0]
fixed2 = [5, 0, 0]
init_mid = [2, 0, 0]   # initial position of the middle Al
final_mid = [3, 0, 0]  # final position of the middle Al

# initial and final states
initial = Atoms('Al3', positions=[fixed1, init_mid, fixed2])
final   = Atoms('Al3', positions=[fixed1, final_mid, fixed2])

# attach EMT calculator
for img in (initial, final):
    img.set_calculator(EMT())

# create 3 images (initial, one interpolated, final)
n_images = 3
images = [initial] + [initial.copy() for _ in range(n_images - 2)] + [final]
for img in images:
    img.set_calculator(EMT())

# NEB setup and linear interpolation
neb = NEB(images)
neb.interpolate()

# optimize the band
opt = BFGS(neb)
opt.run(fmax=0.05)

# print energies of each image
for i, img in enumerate(images):
    print(i, img.get_potential_energy())
