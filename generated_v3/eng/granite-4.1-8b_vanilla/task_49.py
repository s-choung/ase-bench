from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS
from ase.eos import EquationOfState
from ase.lattice.cubic import FaceCenteredCubic
import numpy as np

# Parameters
elements = ['Cu']
a0_range = (2.28, 2.52, 0.02)  # Initial lattice parameters for EOS fitting

# Create bulk FCC copper and perform EOS fitting
bulk = FaceCenteredCubic(elements=elements, size=(4, 4, 4), vacuum=10.0)
bulk.set_calculator(EMT())
calc = bulk.get_calculator()

# Equilibrate the bulk cell to get a good initial lattice constant
opt = BFGS(bulk)
opt.run(fmax=0.05)
L0 = bulk.cell[2, 2] / np.sqrt(2)  # Half of the face diagonal for FCC

# EOS fitting to find equilibrium lattice constant
bulk.set_cell((L0 + a0_range[0], L0 + a0_range[0], L0 + a0_range[0]), True)
energies = []
for a in np.arange(a0_range[0], a0_range[1] + a0_range[2], a0_range[2]):
    bulk.set_cell((a, a, a), scale_atoms=True)
    energies.append(bulk.get_potential_energy())

eos = EquationOfState(energies, np.array([a + a0_range[0] for a in np.arange(a0_range[0], a0_range[1] + a0_range[2], a0_range[2])]))
a_eq, _, _ = eos.fit()

# Create (111) slab with equilibrium lattice constant
slab = FaceCenteredCubic(elements=elements, size=(1, 1, 4), vacuum=8.0)
slab.set_calculator(EMT())
slab.set_cell((a_eq, a_eq, a_eq * 4.0 / np.sqrt(2)), scale_atoms=True)

# Fix the bottom 2 layers
mask = [atom.position[2] < a_eq * 2.0 / np.sqrt(2) for atom in slab]
constraints = FixAtoms(mask=mask)
slab.constraints = constraints

# Optimize the slab
opt = BFGS(slab, trajectory='cu_slab_relax.traj')
opt.run(fmax=0.05)

# Print final energy and average z-coordinate for each layer
energies = slab.get_potential_energy()
positions = slab.get_positions()
z_coords = positions[:, 2]
layer_height = z_coords[-1] - z_coords[0]
layer_intervals = layer_height / 4.0
average_z_per_layer = np.linspace(z_coords[0] + layer_intervals / 2, z_coords[-1] - layer_intervals / 2, 4)

for i, avg_z in enumerate(average_z_per_layer):
    layer_atoms = slab.selective_mask & (abs(z_coords - avg_z) < layer_intervals / 2)
    print(f"Layer {i + 1}: avg_z = {avg_z:.3f} Å, num_atoms = {sum(layer_atoms)}")

print(f"Final slab energy: {energies:.6f} eV")
