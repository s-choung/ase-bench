from ase import Atoms
from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.eos import calculate_eos
from ase.optimize import BFGS
import numpy as np

# 1. Equilibrium lattice constant via EOS
cu = bulk('Cu', 'fcc', a=3.6)
cu.calc = EMT()
eos = calculate_eos(cu, eps=0.04)
a_eq = eos.fit()[0]
print(f'Equilibrium lattice constant: {a_eq:.4f} Ang')

# 2. (111) 4-layer slab
slab = fcc111('Cu', size=(1, 1, 4), a=a_eq, vacuum=10.0)
slab.calc = EMT()
n_atoms = len(slab)
n_per_layer = n_atoms // 4

# 3. Fix bottom 2 layers (z < median of bottom-half z)
z = slab.positions[:, 2]
sorted_z = np.sort(z)
mid = (sorted_z[n_atoms // 2 - 1] + sorted_z[n_atoms // 2]) / 2
mask = slab.positions[:, 2] < mid
slab.set_constraint(mask)

# 4. BFGS relaxation
opt = BFGS(slab, logfile=None)
opt.run(fmax=0.02)

# 5. Print final energy and per-layer avg z
print(f'Final energy: {slab.get_potential_energy():.4f} eV')
zf = slab.positions[:, 2]
order = np.argsort(zf)
for i in range(4):
    z_layer = zf[order[i * n_per_layer:(i + 1) * n_per_layer]]
    print(f'Layer {i+1}: avg z = {np.mean(z_layer):.4f} Ang')
