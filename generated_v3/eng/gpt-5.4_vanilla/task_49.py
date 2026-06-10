from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.constraints import FixAtoms
from ase.optimize import BFGS
import numpy as np

# EOS for Cu FCC bulk
a_vals = np.linspace(3.45, 3.75, 9)
volumes, energies = [], []

for a in a_vals:
    atoms = bulk('Cu', 'fcc', a=a)
    atoms.calc = EMT()
    energies.append(atoms.get_potential_energy())
    volumes.append(atoms.get_volume())

eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit()
a0 = (4.0 * v0) ** (1.0 / 3.0)

# Build Cu(111) slab
slab = fcc111('Cu', size=(2, 2, 4), a=a0, vacuum=10.0)
slab.calc = EMT()

# Fix bottom 2 layers
z = slab.positions[:, 2]
z_unique = np.unique(np.round(z, 6))
z_unique.sort()
bottom_two = z_unique[:2]
mask = np.isin(np.round(z, 6), bottom_two)
slab.set_constraint(FixAtoms(mask=mask))

# Relax
opt = BFGS(slab, logfile=None)
opt.run(fmax=0.02)

# Final energy
energy = slab.get_potential_energy()
print(f'Equilibrium lattice constant a0 = {a0:.6f} Å')
print(f'Final slab energy = {energy:.6f} eV')

# Average z for each layer
z = slab.positions[:, 2]
z_round = np.round(z, 3)
layers = np.unique(z_round)
layers.sort()
for i, zl in enumerate(layers, 1):
    idx = np.where(np.isclose(z_round, zl))[0]
    print(f'Layer {i}: avg z = {z[idx].mean():.6f} Å')
