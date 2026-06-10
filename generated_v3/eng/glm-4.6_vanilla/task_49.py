import numpy as np
from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.optimize import BFGS
from ase.constraints import FixAtoms

# Find equilibrium lattice constant
vols, energies = [], []
for a in np.linspace(3.5, 3.7, 5):
    atoms = bulk('Cu', 'fcc', a=a)
    atoms.calc = EMT()
    vols.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())

eos = EquationOfState(vols, energies)
v0, _, _ = eos.fit()
a0 = (v0 / 4)**(1/3)

# Create slab
slab = fcc111('Cu', a0, size=(1, 1, 4), vacuum=10.0)
slab.calc = EMT()

# Fix bottom 2 layers
z = slab.positions[:, 2]
fixed_indices = np.argsort(z)[:len(slab)//2]
slab.set_constraint(FixAtoms(indices=fixed_indices))

# Relax
BFGS(slab).run(fmax=0.05)

# Output
print(f"Final Energy: {slab.get_potential_energy():.4f} eV")
z_final = slab.positions[:, 2]
sorted_indices = np.argsort(z_final)
n_per_layer = len(slab) // 4

for i in range(4):
    layer_indices = sorted_indices[i*n_per_layer : (i+1)*n_per_layer]
    avg_z = np.mean(z_final[layer_indices])
    print(f"Layer {i+1} avg Z: {avg_z:.3f} Å")
