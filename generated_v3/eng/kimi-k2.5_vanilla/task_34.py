from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.neb import NEB
from ase.optimize import BFGS

slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0)

initial = slab.copy()
add_adsorbate(initial, 'Cu', 2.0, 'fcc')
initial.calc = EMT()
BFGS(initial).run(fmax=0.01)

final = slab.copy()
add_adsorbate(final, 'Cu', 2.0, 'hcp')
final.calc = EMT()
BFGS(final).run(fmax=0.01)

images = [initial]
for _ in range(3):
    images.append(initial.copy())
    images[-1].calc = EMT()
images.append(final)

neb = NEB(images)
neb.interpolate(method='idpp')
BFGS(neb).run(fmax=0.05)

energies = [im.get_potential_energy() for im in images]
barrier = max(energies) - energies[0]
print(f"{barrier:.3f}")
