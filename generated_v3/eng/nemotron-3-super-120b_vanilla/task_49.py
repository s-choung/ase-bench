from ase.build import bulk, surface
from ase.eos import EOS
from ase.constraints import FixAtoms
from ase.optimize import BFGS
from ase.calculators.emt import EMT
import numpy as np

# 1. Equilibrium lattice constant from EOS
a_guess = 3.6
volumes, energies = [], []
for s in np.linspace(0.96, 1.04, 11):
    a = a_guess * s
    atoms = bulk('Cu', 'fcc', a=a, cubic=True)
    atoms.calc = EMT()
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())
eos = EOS(volumes, energies)
v0, _, _ = eos.fit()
a_eq = v0 ** (1.0 / 3.0)  # conventional cubic cell volume = a^3

# 2. Create (111) 4‑layer slab
slab = surface(bulk('Cu', 'fcc', a=a_eq, cubic=True), (1,1,1), layers=4, vacuum=10.0)
slab.calc = EMT()

# 3. Fix bottom two layers
pos = slab.get_positions()
z = pos[:,2]
order = np.argsort(z)
n_per_layer = len(slab) // 4
bottom_idx = order[:2*n_per_layer]
mask = np.zeros(len(slab), dtype=bool)
mask[bottom_idx] = True
slab.set_constraint(FixAtoms(mask=mask))

# 4. BFGS relaxation
dyn = BFGS(slab)
dyn.run(fmax=0.05)

# 5. Results
energy = slab.get_potential_energy()
pos = slab.get_positions()
z = pos[:,2]
order = np.argsort(z)
layer_zs = [z[order[i*n_per_layer:(i+1)*n_per_layer]].mean() for i in range(4)]
print(f'Final energy: {energy:.4f} eV')
for i, zv in enumerate(layer_zs, start=1):
    print(f'Layer {i} average z: {zv:.4f} Å')
