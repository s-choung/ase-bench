from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.neb import NEB

original = fcc111('Cu', (2, 2, 4), vacuum=8.0, a=3.6)
initial = original.copy()
add_adsorbate(initial, 'Cu', 2.0, position='fcc')
final = original.copy()
add_adsorbate(final, 'Cu', 2.0, position='hcp')

images = [initial] + [initial.copy() for _ in range(3)] + [final]
neb = NEB(images)
neb.interpolate(method='idpp')

for img in images:
    img.calc = EMT()

opt = BFGS(neb)
opt.run(fmax=0.05)

energies = [img.get_potential_energy() for img in images]
barrier = max(energies) - energies[0]
print(f"{barrier:.4f} eV")
