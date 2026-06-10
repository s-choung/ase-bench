from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.optimize import BFGS
from ase.constraints import FixAtoms
import numpy as np
b = bulk('Cu', 'fcc', a=3.6, cubic=True)
cell = b.cell
v, e = [], []
for x in np.linspace(0.95, 1.05, 9):
    b.set_cell(cell * x, scale_atoms=True)
    b.calc = EMT()
    v.append(b.get_volume())
    e.append(b.get_potential_energy())
a, _, _ = EquationOfState(v, e).fit()
a_lat = (a / 4)**(1/3)
slab = fcc111('Cu', size=(1, 1, 4), a=a_lat, vacuum=10.0)
slab.calc = EMT()
mask = [t <= 2 for t in slab.get_tags()]
slab.set_constraint(FixAtoms(mask=mask))
BFGS(slab).run(fmax=0.05)
print(slab.get_potential_energy())
z = slab.positions[:, 2]
tags = slab.get_tags()
for i in range(1, 5):
    print(i, np.mean(z[tags == i]))
