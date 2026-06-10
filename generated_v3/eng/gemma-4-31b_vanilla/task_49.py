import numpy as np
from ase import Atoms
from ase.build import bulk, surface, add_adsorbate
from ase.eos import EquationOfState
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FixAtoms

# 1. Equilibrium lattice constant for Cu (FCC)
calc = EMT()
lattice_constants = np.arange(3.4, 3.8, 0.05)
energies = []
for a in lattice_constants:
    atoms = bulk('Cu', 'fcc', a=a)
    atoms.set_calculator(calc)
    energies.append(atoms.get_potential_energy())

eos = EquationOfState(lattice_constants, energies)
a0 = eos.fit().a

# 2. Create (111) 4-layer slab
slab = surface('Cu', (111), layers=4, vacuum=10.0, a=a0)
slab.set_calculator(calc)

# 3. Fix bottom 2 layers (indices 0 to (total/2)-1)
# In ASE surface(), layers are usually stacked along z
z_coords = slab.positions[:, 2]
# Find indices of the 2 lowest layers
mask = z_coords <= np.partition(z_coords, len(z_coords)//2)[len(z_coords)//2 - 1]
slab.set_constraint(FixAtoms(mask=mask))

# 4. BFGS Relaxation
dyn = BFGS(slab, trajectory='relax.traj')
dyn.run(fmax=0.05)

# 5. Output results
print(f"Final Energy: {slab.get_potential_energy():.4f} eV")
z_final = slab.positions[:, 2]
# Group by original layers (roughly sorted by z)
sorted_indices = np.argsort(z_final)
layer_size = len(slab) // 4
for i in range(4):
    layer_z = z_final[sorted_indices[i*layer_size : (i+1)*layer_size]]
    print(f"Layer {i} Avg Z: {np.mean(layer_z):.4f} Å")
