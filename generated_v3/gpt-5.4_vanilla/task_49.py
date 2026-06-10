from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.constraints import FixAtoms
from ase.optimize import BFGS
import numpy as np

a0 = 3.6
scales = np.linspace(0.96, 1.04, 7)
volumes, energies = [], []

for s in scales:
    a = a0 * s
    atoms = bulk('Cu', 'fcc', a=a)
    atoms.calc = EMT()
    energies.append(atoms.get_potential_energy())
    volumes.append(atoms.get_volume())

eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit()
a_opt = (4 * v0) ** (1 / 3)

slab = fcc111('Cu', size=(2, 2, 4), a=a_opt, vacuum=10.0)
z = slab.positions[:, 2]
z_layers = np.unique(np.round(z, 3))
z_layers.sort()
fixed_layers = z_layers[:2]
mask = np.isin(np.round(z, 3), fixed_layers)

slab.set_constraint(FixAtoms(mask=mask))
slab.calc = EMT()

opt = BFGS(slab, logfile=None)
opt.run(fmax=0.02)

energy = slab.get_potential_energy()
z = slab.positions[:, 2]
z_layers = np.unique(np.round(z, 3))
z_layers.sort()

print(f'lattice_constant = {a_opt:.6f} Ang')
print(f'final_energy = {energy:.6f} eV')

for i, zl in enumerate(z_layers, 1):
    layer_mask = np.isclose(z, zl, atol=1e-2)
    print(f'layer_{i}_z_mean = {z[layer_mask].mean():.6f} Ang')
