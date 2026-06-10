from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FixAtoms

# Build 4-layer Cu(111) slab
slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0)

# Tag bottom 2 layers based on z-coordinate
z_sorted = sorted(set(slab.positions[:, 2]))
limit = z_sorted[1]
for atom in slab:
    if atom.position[2] <= limit + 1e-5:
        atom.tag = 1

# Fix atoms with tag 1
slab.set_constraint(FixAtoms(mask=[atom.tag == 1 for atom in slab]))

# Set EMT calculator
slab.calc = EMT()

# Record initial positions of fixed atoms
fixed_indices = [i for i, atom in enumerate(slab) if atom.tag == 1]
initial_coords = slab[fixed_indices].get_positions().copy()

# Run BFGS optimization
BFGS(slab).run(fmax=0.05)

# Record final positions
final_coords = slab[fixed_indices].get_positions()

# Print comparison
print("Initial fixed coords:\n", initial_coords)
print("Final fixed coords:\n", final_coords)
print("Max diff:", (initial_coords - final_coords).max())
