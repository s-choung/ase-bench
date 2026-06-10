import numpy as np
from ase import Atom
from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.optimize import BFGS, FIRE
from ase.mep import NEB
from ase.constraints import FixAtoms

slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0)
cell = slab.get_cell()
z_ad = max(slab.positions[:, 2]) + 2.0

pos1 = cell[0] / 6 + cell[1] / 3
pos1[2] = z_ad
pos2 = cell[0] / 3 + cell[1] / 6
pos2[2] = z_ad

def make_state(pos):
    atoms = slab.copy()
    atoms.append(Atom('Cu', pos))
    z = atoms.positions[:, 2]
    z_thresh = (np.sort(z)[7] + np.sort(z)[8]) / 2
    atoms.set_constraint(FixAtoms(mask=z < z_thresh))
    atoms.calc = EMT()
    return atoms

initial = make_state(pos1)
final = make_state(pos2)

BFGS(initial).run(fmax=0.05)
BFGS(final).run(fmax=0.05)

images = [initial] + [initial.copy() for _ in range(5)] + [final]
neb = NEB(images)
neb.interpolate(method='idpp')

for img in images[1:-1]:
    img.calc = EMT()

FIRE(neb).run(fmax=0.05)

energies = [img.get_potential_energy() for img in images]
barrier = max(energies) - energies[0]
print(f"Energy barrier: {barrier:.3f} eV")
