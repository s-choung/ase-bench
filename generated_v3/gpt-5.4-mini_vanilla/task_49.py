from ase.build import bulk, surface
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FixAtoms
from ase.eos import EquationOfState
import numpy as np

a0 = bulk('Cu', 'fcc', a=3.6).cell.lengths()[0]
a_vals = np.linspace(0.95 * a0, 1.05 * a0, 9)
energies = []

for a in a_vals:
    atoms = bulk('Cu', 'fcc', a=a)
    atoms.calc = EMT()
    energies.append(atoms.get_potential_energy())

eos = EquationOfState(a_vals**3 / 4.0, energies)
v0, e0, B = eos.fit()
a_eq = (4.0 * v0) ** (1.0 / 3.0)

slab = surface(bulk('Cu', 'fcc', a=a_eq), (1, 1, 1), 4, vacuum=10.0)
slab.calc = EMT()

z = slab.positions[:, 2]
layers = np.unique(np.round(z, 3))
layers.sort()
fix_z = layers[:2]
mask = np.isin(np.round(z, 3), fix_z)
slab.set_constraint(FixAtoms(mask=mask))

opt = BFGS(slab, logfile=None)
opt.run(fmax=0.01)

e_final = slab.get_potential_energy()
z = slab.positions[:, 2]
layer_ids = np.unique(np.round(z, 3))
layer_ids.sort()

print(f"Equilibrium lattice constant a = {a_eq:.6f} Å")
print(f"Final energy = {e_final:.6f} eV")
for i, zz in enumerate(layer_ids, 1):
    idx = np.isclose(np.round(z, 3), zz)
    print(f"Layer {i}: <z> = {z[idx].mean():.6f} Å")
