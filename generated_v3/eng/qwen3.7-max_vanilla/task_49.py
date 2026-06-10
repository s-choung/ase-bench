import numpy as np
from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.constraints import FixAtoms
from ase.optimize import BFGS

v, e = [], []
for a in np.linspace(3.4, 3.8, 7):
    cu = bulk('Cu', 'fcc', a=a)
    cu.calc = EMT()
    v.append(cu.get_volume())
    e.append(cu.get_potential_energy())
    
a0 = (4 * EquationOfState(v, e).fit()[0])**(1/3)

slab = fcc111('Cu', a=a0, size=(1, 1, 4), vacuum=10.0)
slab.calc = EMT()

z = slab.positions[:, 2]
layers = np.unique(np.round(z, 2))
slab.set_constraint(FixAtoms(indices=np.where(np.isin(np.round(z, 2), layers[:2]))[0]))

BFGS(slab, logfile=None).run(fmax=0.01)

print(f"Equilibrium a0: {a0:.3f} Å | Final Energy: {slab.get_potential_energy():.4f} eV")
for l in layers:
    print(f"Layer avg z: {z[np.round(z, 2) == l].mean():.4f} Å")
