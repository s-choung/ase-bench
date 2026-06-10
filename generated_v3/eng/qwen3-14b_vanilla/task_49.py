import numpy as np
from ase.build import bulk, surface
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.eos import EquationOfState

# Find equilibrium lattice constant
a_values = np.linspace(3.5, 4.5, 11)
volumes, energies = [], []
for a in a_values:
    atoms = bulk('Cu', 'fcc', a=a, cubic=True)
    atoms.set_calculator(EMT())
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())

eos = EquationOfState(volumes, energies)
v0, e0, _ = eos.fit()
a_eq = v0 ** (1/3)

# Create (111) 4-layer slab
bulk_structure = bulk('Cu', 'fcc', a=a_eq, cubic=True)
slab = surface(bulk_structure, (1, 1, 1), 4, vacuum=10.0)
slab.set_calculator(EMT())

# Fix bottom 2 layers
positions = slab.get_positions()
z = positions[:, 2]
indices = np.argsort(z)
mask = np.zeros(len(slab), bool)
mask[indices[:len(indices)//2]] = True
slab.set_constraint(mask)

# Relax
opt = BFGS(slab)
opt.run(fmax=0.05)

# Print results
print(f"Final energy: {slab.get_potential_energy():.4f} eV")
positions = slab.get_positions()
z = positions[:, 2]
sorted_indices = np.argsort(z)
for i in range(4):
    layer = z[sorted_indices[i::4]]
    print(f"Layer {i+1} average z: {np.mean(layer):.4f} Å")
