import numpy as np
from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.filters import FrechetCellFilter
from ase.optimize import BFGS
from ase.constraints import FixAtoms

# EOS for Cu fcc bulk
a0_guess = 3.6
scales = np.linspace(0.96, 1.04, 9)
volumes, energies, alats = [], [], []

for s in scales:
    a = a0_guess * s
    atoms = bulk('Cu', 'fcc', a=a, cubic=True)
    atoms.calc = EMT()
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())
    alats.append(a)

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()
a_eq = v0 ** (1 / 3)

# Build relaxed bulk at equilibrium lattice constant
bulk_atoms = bulk('Cu', 'fcc', a=a_eq)
bulk_atoms.calc = EMT()
BFGS(FrechetCellFilter(bulk_atoms), logfile=None).run(fmax=0.01)

cellpar = bulk_atoms.get_cell_lengths_and_angles()
a_slab = cellpar[0]

# Build Cu(111) slab
slab = fcc111('Cu', size=(2, 2, 4), a=a_slab, vacuum=10.0)
z = slab.positions[:, 2]
z_sorted = np.sort(np.unique(np.round(z, 6)))
layer_z = z_sorted[:4]

tol = 1e-3
tags = []
for zi in z:
    tags.append(int(np.argmin(np.abs(layer_z - zi))) + 1)
slab.set_tags(tags)

mask = [tag <= 2 for tag in slab.get_tags()]
slab.set_constraint(FixAtoms(mask=mask))
slab.calc = EMT()

BFGS(slab, logfile=None).run(fmax=0.02)

energy = slab.get_potential_energy()
z = slab.positions[:, 2]
tags = slab.get_tags()

print(f'Equilibrium lattice constant a = {a_slab:.6f} Å')
print(f'Final slab energy = {energy:.6f} eV')
for layer in sorted(set(tags)):
    avg_z = z[np.array(tags) == layer].mean()
    print(f'Layer {layer}: average z = {avg_z:.6f} Å')
