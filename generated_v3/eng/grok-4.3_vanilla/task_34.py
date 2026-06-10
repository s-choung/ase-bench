from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.neb import NEB
from ase.optimize import BFGS
slab = fcc111('Cu', (2, 2, 3), vacuum=10)
add_adsorbate(slab, 'Cu', 2.0, 'fcc')
images = [slab]
images += [slab.copy() for _ in range(3)]
images += [slab.copy()]
add_adsorbate(images[-1], 'Cu', 2.0, 'hcp')
neb = NEB(images)
neb.interpolate('idpp')
for img in images:
 img.calc = EMT()
BFGS(neb).run(fmax=0.05)
energies = [img.get_potential_energy() for img in images]
print(max(energies) - energies[0])
