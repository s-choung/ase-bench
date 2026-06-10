from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.eos import calculate_eos
from ase.optimize import BFGS
from ase.constraints import FixAtoms
import numpy as np

# Find equilibrium lattice constant of FCC Cu using EOS
cu_bulk = bulk('Cu', 'fcc', a=3.6)
cu_bulk.calc = EMT()
v0, _, _ = calculate_eos(cu_bulk).fit()
a0 = (4 * v0) ** (1/3)

# Create 4-layer (111) slab with vacuum
slab = fcc111('Cu', size=(1, 1, 4), a=a0, vacuum=10.0)
slab.calc = EMT()

# Fix bottom 2 layers (lowest z-coordinates)
z_coords = slab.get_positions()[:, 2]
fixed_indices = np.argsort(z_coords)[:2]
slab.set_constraint(FixAtoms(indices=fixed_indices))

# Run BFGS surface relaxation
opt = BFGS(slab)
opt.run(fmax=0.01)

# Print final energy
print(f"Final energy: {slab.get_potential_energy():.4f} eV")

# Calculate and print average z-coordinate for each layer
final_z = slab.get_positions()[:, 2]
rounded_z = np.round(final_z, 1)
for i, z_val in enumerate(np.unique(rounded_z)):
    avg_z = np.mean(final_z[rounded_z == z_val])
    print(f"Layer {i+1}: average z = {avg_z:.4f} Å")
