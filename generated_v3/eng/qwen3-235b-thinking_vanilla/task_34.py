from ase import Atom, Atoms
from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.neb import NEB, idpp_interpolate
from ase.optimize import BFGS
from math import sqrt

a = 3.61
slab = fcc111('Cu', size=(3, 3, 3), vacuum=10.0)
z_top = max(slab.positions[:9, 2])

x_fcc = 1.5 * a
y_fcc = 2 * a * sqrt(3) / 3
initial = slab.copy()
initial.append(Atom('Cu', (x_fcc, y_fcc, z_top + 2.0)))

x_hcp = x_fcc + a / 3
y_hcp = y_fcc - a * sqrt(3) / 6
final = slab.copy()
final.append(Atom('Cu', (x_hcp, y_hcp, z_top + 2.0)))

mask = [9 <= i < 27 for i in range(len(initial))]
initial.set_constraint(FixAtoms(mask=mask))
final.set_constraint(FixAtoms(mask=mask))

calc = EMT()
initial.calc = calc
final.calc = calc

for config in [initial, final]:
    BFGS(config).run(fmax=0.01)

images = [initial] + [initial.copy() for _ in range(3)] + [final]
idpp_interpolate(images)
neb = NEB(images)
BFGS(neb).run(fmax=0.05)

energies = [img.get_potential_energy() for img in images]
barrier = max(energies) - energies[0]
print(f"{barrier:.3f}")
