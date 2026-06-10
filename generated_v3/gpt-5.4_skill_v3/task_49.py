import numpy as np
from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.filters import FrechetCellFilter
from ase.optimize import BFGS
from ase.constraints import FixAtoms

cu = bulk('Cu', 'fcc', a=3.6, cubic=True)
cu.calc = EMT()
BFGS(FrechetCellFilter(cu), logfile=None).run(fmax=0.01)

cell0 = cu.get_cell()
volumes, energies, scales = [], [], np.linspace(0.97, 1.03, 7)
for s in scales:
    a = cu.copy()
    a.set_cell(cell0 * s, scale_atoms=True)
    a.calc = EMT()
    volumes.append(a.get_volume())
    energies.append(a.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()
a0 = v0 ** (1 / 3)

slab = fcc111('Cu', size=(2, 2, 4), a=a0, vacuum=10.0)
z = slab.positions[:, 2]
zuniq = np.unique(np.round(z, 6))
zlayers = np.sort(zuniq)
bottom2 = zlayers[:2]
mask = np.isin(np.round(z, 6), bottom2)
slab.set_constraint(FixAtoms(mask=mask))
slab.calc = EMT()

BFGS(slab, logfile=None).run(fmax=0.02)

energy = slab.get_potential_energy()
z = slab.positions[:, 2]
zlayers = np.sort(np.unique(np.round(z, 3)))
layer_means = []
for zl in zlayers:
    sel = np.abs(z - zl) < 0.2
    layer_means.append(z[sel].mean())

print(f'a0 = {a0:.6f} Ang')
print(f'final_energy = {energy:.6f} eV')
for i, zm in enumerate(sorted(layer_means), 1):
    print(f'layer_{i}_z_mean = {zm:.6f} Ang')
