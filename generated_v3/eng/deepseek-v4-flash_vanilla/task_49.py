import numpy as np
from ase import Atoms
from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS
from ase.eos import EOS

# Step 1: Find equilibrium lattice constant for Cu bulk using EMT
a_values = np.linspace(3.5, 3.8, 10)
energies = []
for a in a_values:
    atoms_bulk = bulk('Cu', 'fcc', a=a)
    atoms_bulk.calc = EMT()
    energies.append(atoms_bulk.get_potential_energy())
eos = EOS(a_values, energies)
a0, _, _ = eos.fit()

# Step 2: Build (111) 4-layer slab with the equilibrium lattice constant
slab = fcc111('Cu', size=(1,1,4), a=a0, vacuum=10.0)

# Step 3: Attach EMT calculator
slab.calc = EMT()

# Step 4: Fix bottom 2 layers (lowest z coordinates)
pos = slab.positions
z = pos[:, 2]
sorted_indices = np.argsort(z)
fix_indices = sorted_indices[:2]  # bottom two atoms
slab.set_constraint(FixAtoms(indices=fix_indices))

# Step 5: Run BFGS relaxation
opt = BFGS(slab)
opt.run(fmax=0.01)

# Step 6: Print final energy and average z per layer
print(f"Final energy: {slab.get_potential_energy():.6f} eV")
unique_z = np.unique(np.round(z, decimals=6))
unique_z.sort()
for i, z_layer in enumerate(unique_z):
    mask = np.isclose(z, z_layer, atol=1e-5)
    avg_z = np.mean(z[mask])
    print(f"Layer {i+1} (bottom to top): average z = {avg_z:.4f} Å")
