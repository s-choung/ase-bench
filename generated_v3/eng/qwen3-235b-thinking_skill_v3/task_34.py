from ase import Atoms
from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.neb import NEB

slab = fcc111('Cu', size=(3, 3, 4), a=3.615, vacuum=10.0)
initial = slab.copy()
add_adsorbate(initial, 'Cu', 1.8, 'fcc')
final = slab.copy()
add_adsorbate(final, 'Cu', 1.8, 'hcp')

mask = [i < 18 for i in range(len(initial))]
initial.set_constraint(mask)
final.set_constraint(mask)

initial.calc = final.calc = EMT()
BFGS(initial, fmax=0.01).run()
BFGS(final, fmax=0.01).run()

images = [initial] + [initial.copy() for _ in range(3)] + [final]
for img in images:
    img.calc = EMT()
neb = NEB(images)
neb.interpolate('idpp')
BFGS(neb, fmax=0.1).run()
barrier = max(img.get_potential_energy() for img in images) - images[0].get_potential_energy()
print(barrier)
