from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.eos import EquationOfState
import numpy as np

# Step 1: Find equilibrium lattice constant for Cu FCC bulk
volumes = []
energies = []
for a in np.linspace(3.4, 3.8, 5):
    atoms = bulk('Cu', 'fcc', a=a)
    atoms.calc = EMT()
    energies.append(atoms.get_potential_energy())
    volumes.append(atoms.get_volume())

eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit()
a0 = (v0 * 4) ** (1/3)  # Convert FCC volume to lattice constant

# Step 2: Create 4-layer Cu(111) slab
slab = fcc111('Cu', size=(2, 2, 4), vacuum=10, a=a0)

# Step 3: Fix bottom 2 layers and relax
z_pos = slab.positions[:, 2]
layer_indices = [np.where((z_pos > min(z_pos) + i*0.2) & (z_pos < min(z_pos) + (i+1)*0.2))[0] for i in range(4)]
for i in [0, 1]:  # Fix bottom two layers
    slab.constraints = [a.constraints[0] for a in slab if a.index in layer_indices[i]]
slab.calc = EMT()
opt = BFGS(slab)
opt.run(fmax=0.05)

# Step 4: Print results
print(f"Final energy: {slab.get_potential_energy():.6f} eV")
for i, indices in enumerate(layer_indices):
    avg_z = np.mean(slab.positions[indices, 2])
    print(f"Layer {i} avg z: {avg_z:.6f} Å")
