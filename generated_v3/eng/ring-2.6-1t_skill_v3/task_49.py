from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.optimize import BFGS
from ase.constraints import FixAtoms
import numpy as np

# ---- EOS for Cu FCC bulk ----
atoms0 = bulk('Cu', 'fcc', a=3.6, cubic=True)   # 4‑atom conventional cell
cell0 = atoms0.get_cell()
scales = np.linspace(0.95, 1.05, 7)
volumes, energies = [], []
for s in scales:
    a = atoms0.copy()
    a.set_cell(cell0 * s, scale_atoms=True)
    a.calc = EMT()
    volumes.append(a.get_volume())
    energies.append(a.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()
a_eq = v0 ** (1/3)               # equilibrium lattice constant

# ---- (111) 4‑layer slab ----
slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0, a=a_eq)
slab.calc = EMT()

# fix the bottom two layers
z = slab.positions[:, 2]
mask = z < np.median(z)          # lower half = 2 layers
slab.set_constraint(FixAtoms(mask=mask))

# relax the surface
opt = BFGS(slab)
opt.run(fmax=0.05)

# ---- output ----
print('Final energy:', slab.get_potential_energy())

# average z per layer
z = slab.positions[:, 2]
rounded = np.round(z, decimals=6)
unique = np.sort(np.unique(rounded))
for i, zv in enumerate(unique):
    idx = np.where(rounded == zv)[0]
    avgz = np.mean(z[idx])
    print(f'Layer {i+1}: avg z = {avgz:.6f}')
