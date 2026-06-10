import numpy as np
from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.optimize import BFGS
from ase.constraints import FixAtoms

# Determine equilibrium lattice constant
a_values = np.linspace(3.5, 3.8, 5)
volumes, energies = [], []

for a in a_values:
    atoms = bulk('Cu', 'fcc', a=a)
    atoms.calc = EMT()
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())

eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit()
a0 = v0 ** (1/3.)

# Create (111) 4-layer slab
slab = fcc111('Cu', (2, 2, 4), a=a0, vacuum=10.0)
slab.calc = EMT()

# Fix bottom 2 layers
positions = slab.get_positions()
zs = positions[:, 2]
sorted_indices = np.argsort(zs)
fixed_indices = sorted_indices[:len(zs)//2]
slab.set_constraint(FixAtoms(indices=fixed_indices))

# Relaxation
BFGS(slab).run(fmax=0.05)

# Output results
print(f"Final energy: {slab.get_potential_energy():.4f} eV")
positions = slab.get_positions()
zs = positions[:, 2]
sorted_indices = np.argsort(zs)
n = len(zs)
n_per_group = n // 4

for i in range(4):
    start, end = i * n_per_group, (i + 1) * n_per_group
    group = sorted_indices[start:end]
    avg_z = positions[group].mean(axis=0)[2]
    print(f"Layer {i+1} average z: {avg_z:.3f} Å")
