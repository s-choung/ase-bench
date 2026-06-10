from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.mep import NEB
from ase.optimize import BFGS
import numpy as np

slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0, a=3.6)

initial = slab.copy()
add_adsorbate(initial, 'Cu', height=1.8, position='fcc')
initial.calc = EMT()
BFGS(initial).run(fmax=0.05)

final = slab.copy()
final_positions = initial.get_positions().copy()
final_positions[-1] += np.array([1.2, 0.7, 0.0])
final.set_positions(final_positions)
final.calc = EMT()
BFGS(final).run(fmax=0.05)

images = [initial]
for _ in range(5):
    images.append(initial.copy())
images.append(final)

neb = NEB(images)
neb.interpolate(method='idpp')

for img in images[1:-1]:
    img.calc = EMT()

opt = BFGS(neb)
opt.run(fmax=0.05)

energies = np.array([img.get_potential_energy() for img in images])
barrier = energies.max() - energies[0]
print(f'Energy barrier: {barrier:.3f} eV')
