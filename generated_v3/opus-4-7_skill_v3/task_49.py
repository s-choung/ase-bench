import numpy as np
from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS
from ase.eos import EquationOfState

cu = bulk('Cu', 'fcc', a=3.6, cubic=True)
cu.calc = EMT()
cell0 = cu.get_cell()
n = len(cu)

volumes, energies = [], []
for x in np.linspace(0.95, 1.05, 9):
    a = cu.copy()
    a.set_cell(cell0 * x, scale_atoms=True)
    a.calc = EMT()
    volumes.append(a.get_volume())
    energies.append(a.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()
a0 = (v0 * 4 / n) ** (1/3) * (n/4) ** 0 
a0 = (v0 / (n/4)) ** (1/3)
print(f"EOS v0 = {v0:.4f} Å^3, a0 = {a0:.4f} Å")

slab = fcc111('Cu', size=(2, 2, 4), a=a0, vacuum=10.0)
tags = slab.get_tags()
mask = [t >= 3 for t in tags]
slab.set_constraint(FixAtoms(mask=mask))
slab.calc = EMT()

opt = BFGS(slab)
opt.run(fmax=0.02)

E = slab.get_potential_energy()
print(f"Final slab energy = {E:.4f} eV")

z = slab.get_positions()[:, 2]
for layer in sorted(set(tags)):
    idx = [i for i, t in enumerate(tags) if t == layer]
    print(f"Layer (tag={layer}): <z> = {z[idx].mean():.4f} Å")
