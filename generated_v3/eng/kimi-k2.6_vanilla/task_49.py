import numpy as np
from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.eos import EquationOfState
from ase.optimize import BFGS

V, E = [], []
for a in np.linspace(3.4, 3.8, 9):
    atoms = bulk('Cu', 'fcc', a=a, cubic=True)
    atoms.calc = EMT()
    V.append(atoms.get_volume())
    E.append(atoms.get_potential_energy())

v0, _, _ = EquationOfState(V, E).fit()
a0 = v0 ** (1 / 3)

slab = fcc111('Cu', size=(1, 1, 4), a=a0, vacuum=10.0)
slab.calc = EMT()
slab.set_constraint(FixAtoms(mask=[t <= 2 for t in slab.get_tags()]))

BFGS(slab, logfile=None).run(fmax=0.01)

print(f"Final energy: {slab.get_potential_energy():.4f} eV")
tags = slab.get_tags()
for tag in range(1, 5):
    z_avg = slab.positions[tags == tag, 2].mean()
    print(f"Layer {tag}: avg z = {z_avg:.4f} Å")
