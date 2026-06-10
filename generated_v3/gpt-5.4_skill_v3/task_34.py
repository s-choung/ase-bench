from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.mep import NEB
from ase.optimize import BFGS
import numpy as np

a = 3.615
size = (2, 2, 4)
vacuum = 10.0
height = 2.0

initial = fcc111('Cu', size=size, a=a, vacuum=vacuum)
initial.set_constraint(FixAtoms(mask=[atom.tag > 2 for atom in initial]))
add_adsorbate(initial, 'Cu', height=height, position='fcc')

final = initial.copy()
xy = final.get_positions()[-1, :2].copy()
cell = final.get_cell()
shift = (cell[0, :2] + cell[1, :2]) / 3.0
final.positions[-1, :2] = xy + shift

images = [initial] + [initial.copy() for _ in range(5)] + [final]
for img in images:
    img.calc = EMT()

neb = NEB(images)
neb.interpolate(method='idpp')

opt = BFGS(neb, logfile=None, trajectory=None)
opt.run(fmax=0.05)

energies = [img.get_potential_energy() for img in images]
barrier = max(energies) - energies[0]
print(barrier)
