from ase import Atoms
from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.optimize import BFGS
from ase.constraints import FixAtoms
import numpy as np
from collections import defaultdict

# ---------- 1. EOS for bulk Cu (FCC) ----------
a0 = 3.6                                 # initial guess
a_vals = a0 * (1 + np.linspace(-0.05, 0.05, 7))
volumes, energies = [], []
for a in a_vals:
    b = bulk('Cu', 'fcc', a=a0)           # prototype
    b.set_cell([a, a, a], scale_atoms=True)
    b.calc = EMT()
    volumes.append(b.get_volume())
    energies.append(b.get_potential_energy())

eos = EquationOfState(volumes, energies)
v_eq, _, _ = eos.fit()
a_eq = v_eq ** (1/3)                     # equilibrium lattice constant

# ---------- 2. Build 4‑layer (111) slab ----------
slab = fcc111('Cu', size=(2, 2, 4), a=a_eq, vacuum=10.0)
slab.calc = EMT()

# ---------- 3. Fix the bottom two layers ----------
fix = FixAtoms(indices=[i for i, a in enumerate(slab) if a.tag <= 1])
slab.set_constraint(fix)

# ---------- 4. Relax with BFGS ----------
dyn = BFGS(slab, trajectory=None)
dyn.run(fmax=0.05)

# ---------- 5. Output ----------
print(f'Final energy = {slab.get_potential_energy():.4f} eV')

layer_z = defaultdict(list)
for a in slab:
    layer_z[a.tag].append(a.position[2])

for lyr in sorted(layer_z):
    avg = sum(layer_z[lyr]) / len(layer_z[lyr])
    print(f'Layer {lyr}: <z> = {avg:.4f} Å')
