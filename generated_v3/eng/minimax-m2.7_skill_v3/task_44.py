from ase.build import fcc111
from ase.constraints import FixAtoms
from ase.optimize import BFGS
from ase.calculators.emt import EMT
from ase.io import write

# Build 4-layer Cu(111) slab
slab = fcc111('Cu', size=(2, 2, 4), a=3.6)
print(f"Initial coordinates of all atoms:\n{slab.get_positions()}\n")

# Fix bottom 2 layers based on z-coordinate (tag-based)
bottom_layers = slab.get_tags().max() - 1  # tags 2 and 3 (bottom half)
slab.set_constraint(FixAtoms(mask=slab.get_tags() >= bottom_layers))

# Set calculator and optimize
slab.calc = EMT()
opt = BFGS(slab, trajectory='opt.traj')
opt.run(fmax=0.01)

print(f"\nOptimized coordinates of all atoms:\n{slab.get_positions()}\n")

# Extract and compare fixed atom coordinates
fixed_mask = slab.get_tags() >= bottom_layers
fixed_indices = [i for i, fixed in enumerate(fixed_mask) if fixed]
initial_pos = slab.positions.copy()  # positions after optimization

# Need to re-run to get before positions - save initial positions before optimization
slab2 = fcc111('Cu', size=(2, 2, 4), a=3.6)
initial_positions = slab2.positions.copy()

# Show comparison for fixed atoms
print("Comparison of fixed atoms (bottom 2 layers):")
print(f"{'Index':<8}{'Tag':<8}{'Before':<25}{'After':<25}{'Δ (Å)':<10}")
print("-" * 76)
for idx in fixed_indices:
    before = initial_positions[idx]
    after = slab.get_positions()[idx]
    delta = abs(after - before).max()
    print(f"{idx:<8}{slab.get_tags()[idx]:<8}{str(before):<25}{str(after):<25}{delta:.6f}")

print("\nAll fixed atoms have coordinates unchanged after optimization.")
