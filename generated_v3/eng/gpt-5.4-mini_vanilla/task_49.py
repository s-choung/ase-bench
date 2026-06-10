from ase.build import bulk, surface
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.eos import EquationOfState
from ase.optimize import BFGS
from ase.io import write
import numpy as np

# EOS for FCC Cu
a_vals = np.linspace(3.4, 3.8, 9)
energies = []
for a in a_vals:
    atoms = bulk('Cu', 'fcc', a=a)
    atoms.calc = EMT()
    energies.append(atoms.get_potential_energy())

eos = EquationOfState(a_vals, energies)
v0, e0, B = eos.fit()
a0 = (4.0 * v0) ** (1.0 / 3.0)

print(f"Equilibrium lattice constant a0 = {a0:.6f} Å")

# Build 4-layer (111) slab
slab = surface(bulk('Cu', 'fcc', a=a0), (1, 1, 1), 4, vacuum=10.0)
slab.calc = EMT()

# Fix bottom 2 layers
z = slab.positions[:, 2]
unique_z = np.unique(np.round(z, 8))
layer_ids = np.zeros(len(slab), dtype=int)
for i, zi in enumerate(unique_z):
    layer_ids[np.isclose(z, zi)] = i
mask = layer_ids < 2
slab.set_constraint(FixAtoms(mask=mask))

# Relax
opt = BFGS(slab, logfile=None)
opt.run(fmax=0.01)

# Results
Efinal = slab.get_potential_energy()
print(f"Final energy = {Efinal:.6f} eV")

z = slab.positions[:, 2]
unique_z = np.unique(np.round(z, 8))
for i, zi in enumerate(unique_z):
    avg_z = z[np.isclose(z, zi)].mean()
    print(f"Layer {i+1}: avg z = {avg_z:.6f} Å")
