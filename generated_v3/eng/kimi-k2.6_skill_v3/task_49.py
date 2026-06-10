from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.eos import EquationOfState
from ase.optimize import BFGS
import numpy as np

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
cell = atoms.get_cell()
v, e = [], []
for x in np.linspace(0.95, 1.05, 7):
    a = atoms.copy()
    a.set_cell(cell * x, scale_atoms=True)
    a.calc = EMT()
    v.append(a.get_volume())
    e.append(a.get_potential_energy())

v0, _, _ = EquationOfState(v, e).fit()
a0 = v0 ** (1.0 / 3.0)

slab = fcc111('Cu', size=(1, 1, 4), a=a0, vacuum=10.0)
slab.calc = EMT()
slab.set_constraint(FixAtoms(mask=[a.tag >= 3 for a in slab]))
BFGS(slab).run(fmax=0.05)

print(f"Energy: {slab.get_potential_energy():.4f} eV")
tags = slab.get_tags()
for tag in sorted(set(tags)):
    print(f"Layer {tag}: {slab.positions[tags == tag, 2].mean():.3f} Å")
