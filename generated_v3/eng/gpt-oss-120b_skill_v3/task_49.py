#!/usr/bin/env python
import numpy as np
from ase import Atoms
from ase.build import bulk, fcc111, add_vacuum
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FixAtoms
from ase.eos import EquationOfState

# --------- 1. EOS for bulk Cu (EMT) ----------
a_guess = 3.6  # Å
cu_bulk = bulk('Cu', 'fcc', a=a_guess)
cu_bulk.calc = EMT()

volumes, energies = [], []
for s in np.linspace(0.94, 1.06, 7):
    atoms = cu_bulk.copy()
    atoms.set_cell(cu_bulk.get_cell() * s, scale_atoms=True)
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()
a_eq = v0 ** (1.0 / 3.0)  # equilibrium lattice constant (cubic cell)

print(f'Equilibrium lattice constant a = {a_eq:.4f} Å')

# --------- 2. Build 4‑layer Cu(111) slab ----------
slab = fcc111('Cu', size=(2, 2, 4), a=a_eq, vacuum=10.0)
slab.calc = EMT()

# --------- 3. Fix bottom two layers ----------
z = slab.positions[:, 2]
z_unique = np.unique(np.round(z, 5))
threshold = z_unique[1] + 1e-5  # up to the second layer
mask = z <= threshold
slab.set_constraint(FixAtoms(mask=mask))

# --------- 4. Surface relaxation ----------
BFGS(slab).run(fmax=0.05)

# --------- 5. Output results ----------
energy = slab.get_potential_energy()
print(f'Final total energy = {energy:.6f} eV')

# average z per layer (after relaxation)
z = slab.positions[:, 2]
z_unique = np.unique(np.round(z, 5))
layer_averages = []
for zc in z_unique:
    layer_averages.append(z[abs(z - zc) < 1e-4].mean())

for i, z_avg in enumerate(layer_averages, 1):
    print(f'Layer {i:>2}:  <z> = {z_avg:.4f} Å')
