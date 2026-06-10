from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.mep import NEB
from ase.optimize import BFGS
from ase.constraints import FixAtoms

initial = fcc111('Cu', (2, 2, 3), vacuum=10)
add_adsorbate(initial, 'Cu', 1.8, 'fcc')
initial.set_constraint(FixAtoms(indices=[a.index for a in initial if a.tag > 2]))
initial.calc = EMT()
BFGS(initial).run(fmax=0.05)

final = initial.copy()
final[-1].position[:2] += [0.8, 0.46]
final.calc = EMT()
BFGS(final).run(fmax=0.05)

images = [initial] + [initial.copy() for _ in range(5)] + [final]
for img in images[1:-1]:
    img.calc = EMT()
neb = NEB(images)
neb.interpolate(method='idpp')
BFGS(neb).run(fmax=0.05)

energies = [img.get_potential_energy() for img in images]
print(max(energies) - energies[0])
