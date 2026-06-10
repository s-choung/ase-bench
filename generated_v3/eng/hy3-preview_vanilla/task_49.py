import numpy as np
from ase.build import bulk, surface
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS

# Find equilibrium lattice constant for Cu FCC
a_vals = np.linspace(3.5, 3.7, 10)
energies = []
for a in a_vals:
    cu = bulk('Cu', 'fcc', a=a, cubic=True)
    cu.calc = EMT()
    energies.append(cu.get_potential_energy())
coeffs = np.polyfit(a_vals, energies, 2)
a_eq = -coeffs[1] / (2 * coeffs[0])

# Create 4-layer (111) slab
slab = surface('Cu', 'fcc', (1, 1, 1), layers=4, vacuum=10.0)
slab.cell[2, 2] = slab.cell[2, 2] + 10.0  # ensure vacuum
slab.center()
slab.calc = EMT()

# Fix bottom 2 layers (atoms with smallest z-coordinates)
z_positions = slab.get_positions()[:, 2]
sorted_indices = np.argsort(z_positions)
fix_indices = sorted_indices[:8]  # 2 layers * 4 atoms/layer
constraint = FixAtoms(indices=fix_indices)
slab.set_constraint(constraint)

# Relax with BFGS
dyn = BFGS(slab, trajectory='relax.traj')
dyn.run(fmax=0.01)

# Output results
print(f"Final energy: {slab.get_potential_energy():.6f} eV")
z_layers = []
for i in range(4):
    layer_indices = sorted_indices[i*4:(i+1)*4]
    z_avg = np.mean(slab.get_positions()[layer_indices, 2])
    z_layers.append(z_avg)
    print(f"Layer {i+1} average z: {z_avg:.4f} Å")
