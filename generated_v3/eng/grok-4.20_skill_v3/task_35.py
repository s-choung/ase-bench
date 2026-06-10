from ase import Atoms
from ase.calculators.emt import EMT
from ase.mep import NEB
from ase.optimize import BFGS

# Initial: Al at (0,0,0), (3.5,0,0), third at (1.0,0,0)
initial = Atoms('Al3', positions=[[0,0,0], [3.5,0,0], [1.0,0,0]], cell=[7,7,7], pbc=True)
initial.calc = EMT()

# Final: third Al at (2.5,0,0)
final = Atoms('Al3', positions=[[0,0,0], [3.5,0,0], [2.5,0,0]], cell=[7,7,7], pbc=True)
final.calc = EMT()

images = [initial] + [initial.copy() for _ in range(3)] + [final]
for img in images[1:-1]:
    img.calc = EMT()

neb = NEB(images)
neb.interpolate()

print('Initial energies:')
for i, img in enumerate(images):
    e = img.get_potential_energy()
    print(f'Image {i}: {e:.6f} eV')

opt = BFGS(neb, trajectory='al_neb.traj')
opt.run(fmax=0.05)

print('\nFinal NEB energies:')
for i, img in enumerate(images):
    e = img.get_potential_energy()
    print(f'Image {i}: {e:.6f} eV')
