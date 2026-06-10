import numpy as np
from ase.build import bulk, fcc111, stack
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.optimize import BFGS

# 1. Find equilibrium lattice constant via EOS
lat_range = np.linspace(3.5, 4.0, 11)
energies = []
for a in lat_range:
    atoms = bulk('Cu', 'fcc', a, cubic=True)
    atoms.calc = EMT()
    energies.append(atoms.get_potential_energy())

e0, v0 = EquationOfState(lat_range**3, energies).fit()
a_eq = v0**(1/3)
print(f"Equilibrium lattice constant: {a_eq:.4f} Å")

# 2. Create (111) 4-layer slab
slab = fcc111('Cu', size=(3, 3, 4), vacuum=10.0, a=a_eq)
slab.calc = EMT()

# 3. Fix bottom 2 layers
# Layer index is determined by z-coordinate
z_coords = slab.positions[:, 2]
z_threshold = np.sort(z_coords)[1] # index 1 of sorted z
mask = z_coords <= z_threshold
slab.set_constraint(ase.constraints.FixAtoms(mask=mask)) if 'ase.constraints' in globals() else None
# Re-importing constraint locally to ensure script runs if not in namespace
from ase.constraints import FixAtoms
slab.set_constraint(FixAtoms(mask=mask))

# 4. BFGS Surface Relaxation
opt = BFGS(slab)
opt.run(fmax=0.05)

# 5. Output results
print(f"Final Energy: {slab.get_potential_energy():.4f} eV")

# Calculate average z for each layer
layers = []
z_vals = slab.positions[:, 2]
# Group by unique z values (approximate due to float precision)
unique_z = np.unique(np.round(z_vals, 2))
for z in unique_z:
    layer_z = z_vals[np.abs(z_vals - z) < 0.1]
    layers.append(np.mean(layer_z))

for i, z_avg in enumerate(layers):
    print(f"Layer {i} average z: {z_avg:.4f}")
