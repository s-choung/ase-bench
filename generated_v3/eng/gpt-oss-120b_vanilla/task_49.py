#!/usr/bin/env python3
import numpy as np
from ase import Atoms
from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS
from ase.eos import EquationOfState

# ----- 1. Equilibrium lattice constant of Cu (fcc) -----
calc = EMT()
a_guess = 3.6                                   # Å, reasonable Cu lattice constant
cu_bulk = bulk('Cu', 'fcc', a=a_guess)
volumes = []
energies = []
scale_factors = np.linspace(0.94, 1.06, 9)       # ≈ ±6 % around a_guess
for s in scale_factors:
    cu = cu_bulk.copy()
    cu.set_cell(cu.get_cell() * s, scale_atoms=True)
    cu.set_calculator(calc)
    e = cu.get_potential_energy()
    volumes.append(cu.get_volume())
    energies.append(e)

eos = EquationOfState(volumes, energies, eos='birch')
v0, e0, B = eos.fit()
a0 = v0 ** (1 / 3)                              # a0 in Å for the conventional cell
print(f'Equilibrium lattice constant a0 = {a0:.4f} Å')

# ----- 2. Build 4‑layer Cu(111) slab with that a0 -----
slab = fcc111('Cu', size=(1, 1, 4), a=a0, vacuum=10.0, orthogonal=True)
slab.set_calculator(calc)

# ----- 3. Fix bottom two layers -----
z_vals = slab.get_positions()[:, 2]
# unique layer heights (tolerance to avoid floating‑point noise)
layers = np.unique(np.round(z_vals, 5))
# mask atoms belonging to the two lowest layers
mask = np.isin(np.round(z_vals, 5), layers[:2])
slab.set_constraint(FixAtoms(mask=mask))

# ----- 4. Surface relaxation with BFGS -----
dyn = BFGS(slab, logfile=None)
dyn.run(fmax=0.01)

# ----- 5. Output results -----
final_energy = slab.get_potential_energy()
print(f'Final relaxed energy = {final_energy:.6f} eV')

# compute average z for each original layer after relaxation
z_relaxed = slab.get_positions()[:, 2]
layer_means = {}
for i, z0 in enumerate(layers):
    sel = np.isclose(z_relaxed, z0, atol=0.2)   # tolerance larger than thermal noise
    if sel.any():
        layer_means[i+1] = z_relaxed[sel].mean()
for i in sorted(layer_means):
    print(f'Layer {i:1d} average z = {layer_means[i]:.4f} Å')
