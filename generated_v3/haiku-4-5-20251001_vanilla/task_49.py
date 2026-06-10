from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.optimize import BFGS
from ase.constraints import FixAtoms
import numpy as np

# Step 1: Get lattice constant from EOS
cu_bulk = bulk('Cu', 'fcc', a=3.6)
cu_bulk.calc = EMT()

cell_params = np.linspace(3.4, 3.8, 5)
energies = []

for a in cell_params:
    cu = bulk('Cu', 'fcc', a=a)
    cu.calc = EMT()
    energies.append(cu.get_potential_energy())

eos = EquationOfState(cell_params, energies)
v0, e0, B = eos.fit()
a_opt = (v0 * 4) ** (1/3)

print(f"Optimized lattice constant: {a_opt:.6f} Å")

# Step 2: Create (111) slab with 4 layers
slab = fcc111('Cu', size=(3, 3, 4), a=a_opt, vacuum=10.0)
slab.calc = EMT()

# Step 3: Fix bottom 2 layers
z_coords = slab.get_positions()[:, 2]
z_min = z_coords.min()
layer_height = a_opt / np.sqrt(3)

fixed_atoms = []
for i, z in enumerate(z_coords):
    if z - z_min < 2 * layer_height + 0.1:
        fixed_atoms.append(i)

constraint = FixAtoms(indices=fixed_atoms)
slab.set_constraint(constraint)

# Step 4: BFGS relaxation
dyn = BFGS(slab, trajectory='slab_relax.traj')
dyn.run(fmax=0.01)

# Step 5: Print results
final_energy = slab.get_potential_energy()
print(f"\nFinal energy: {final_energy:.6f} eV")

# Calculate average z-coordinate for each layer
positions = slab.get_positions()
z_coords = positions[:, 2]
z_sorted = np.sort(np.unique(np.round(z_coords, 3)))

print("\nLayer z-coordinate averages:")
for i, z_ref in enumerate(z_sorted[-4:], 1):
    layer_atoms = z_coords[np.abs(z_coords - z_ref) < 0.5]
    avg_z = np.mean(layer_atoms)
    print(f"Layer {i}: {avg_z:.6f} Å")
