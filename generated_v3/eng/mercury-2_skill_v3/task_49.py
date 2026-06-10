import numpy as np
from ase import units
from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FixAtoms
from ase.eos import EquationOfState

# 1. EOS for Cu bulk
a0 = 3.6
atoms = bulk('Cu', 'fcc', a=a0)
atoms.calc = EMT()
scale = np.linspace(0.94, 1.06, 7)
vol, eng = [], []
for s in scale:
    slab = atoms.copy()
    slab.set_cell(atoms.get_cell() * s, scale_atoms=True)
    vol.append(slab.get_volume())
    eng.append(slab.get_potential_energy())
eos = EquationOfState(vol, eng, eos='birchmurnaghan')
v0, _, _ = eos.fit()
a_eq = v0 ** (1/3)
print('Equilibrium a = %.4f Å' % a_eq)

# 2. Build 4‑layer (111) slab with equilibrium a
slab = fcc111('Cu', size=(2, 2, 4), a=a_eq, vacuum=10.0)
slab.calc = EMT()

# 3. Fix bottom 2 layers
z = slab.positions[:, 2]
idx = np.argsort(z)
n_layer = len(slab) // 4
mask = np.zeros(len(slab), bool)
mask[idx[:2 * n_layer]] = True
slab.set_constraint(FixAtoms(mask=mask))

# 4. Relax surface
BFGS(slab).run(fmax=0.05)

# 5. Output
energy = slab.get_potential_energy()
print('Final energy = %.6f eV' % energy)

# average z per layer
z_sorted = slab.positions[idx, 2]
for i in range(4):
    layer_z = z_sorted[i*n_layer:(i+1)*n_layer]
    print('Layer %d avg z = %.4f Å' % (i+1, layer_z.mean()))
