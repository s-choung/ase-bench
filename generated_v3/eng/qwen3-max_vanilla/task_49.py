from ase import Atoms
from ase.calculators.emt import EMT
from ase.build import bulk, fcc111
from ase.optimize import BFGS
from ase.eos import EquationOfState
import numpy as np

# Step 1: Find equilibrium lattice constant for Cu FCC using EOS
volumes = []
energies = []
for a in np.linspace(3.5, 3.7, 7):
    cu = bulk('Cu', 'fcc', a=a)
    cu.calc = EMT()
    volumes.append(cu.get_volume())
    energies.append(cu.get_potential_energy())

eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit()
a0 = (4 * v0)**(1/3)

# Step 2: Create 4-layer (111) slab with lattice constant a0
slab = fcc111('Cu', size=(1, 1, 4), a=a0, vacuum=10.0)
slab.calc = EMT()

# Step 3: Fix bottom 2 layers
positions = slab.get_positions()
z_coords = positions[:, 2]
z_sorted = np.sort(z_coords)
fix_height = (z_sorted[1] + z_sorted[2]) / 2  # Between 2nd and 3rd layer
from ase.constraints import FixAtoms
mask = z_coords < fix_height + 0.1
slab.set_constraint(FixAtoms(mask=mask))

# Step 4: Relax with BFGS
opt = BFGS(slab, logfile=None)
opt.run(fmax=0.01)

# Step 5: Print final energy and average z per layer
print(f"Final energy: {slab.get_potential_energy():.6f} eV")
z_coords = slab.get_positions()[:, 2]
layer_indices = [0, 1, 2, 3]
avg_z = [np.mean(z_coords[slab.numbers == 29][i::4]) for i in layer_indices]
for i, z in enumerate(avg_z):
    print(f"Layer {i+1} avg z: {z:.6f} Å")
