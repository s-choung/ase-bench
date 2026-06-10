from ase import Atoms
from ase.build import fcc111
from ase.constraints import FixAtoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS

slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0)
for a in slab:
    a.tag = a.index // 4  # tag bottom 2 layers

fixed_mask = [a.tag >= 2 for a in slab]
fixed_indices = [a.index for a in slab if a.tag >= 2]

initial_positions = slab.positions[fixed_indices].copy()
slab.set_constraint(FixAtoms(mask=fixed_mask))
slab.calc = EMT()

opt = BFGS(slab, trajectory='opt.traj')
opt.run(fmax=0.05)

final_positions = slab.positions[fixed_indices]

print("Initial positions of fixed atoms:")
print(initial_positions)
print("Final positions of fixed atoms:")
print(final_positions)

if np.allclose(initial_positions, final_positions):
    print("Fixed atoms did not move.")
else:
    print("Fixed atoms moved.")
