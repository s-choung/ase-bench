from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.neb import NEB
from ase.optimize import BFGS, FIRE

slab = fcc111('Cu', size=(3, 3, 4), a=3.61, vacuum=10.0)

initial = slab.copy()
add_adsorbate(initial, 'Cu', 1.8, position='fcc')
initial.set_constraint(FixAtoms(indices=list(range(len(initial)-1))))
initial.calc = EMT()
BFGS(initial, logfile=None).run(fmax=0.05)

final = slab.copy()
add_adsorbate(final, 'Cu', 1.8, position='hcp')
final.set_constraint(FixAtoms(indices=list(range(len(final)-1))))
final.calc = EMT()
BFGS(final, logfile=None).run(fmax=0.05)

images = [initial]
for _ in range(3):
    images.append(initial.copy())
images.append(final)

for image in images[1:4]:
    image.calc = EMT()

neb = NEB(images)
neb.idpp_interpolate()
FIRE(neb, logfile=None).run(fmax=0.05)

energies = [image.get_potential_energy() for image in images]
print(max(energies) - energies[0])
