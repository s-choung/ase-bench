from ase.build import fcc111, add_vacuum
from ase.constraints import FixAtoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# Create 4-layer Cu(111) slab
slab = fcc111('Cu', size=(1, 1, 4), a=3.61, vacuum=10.0)

# Fix bottom 2 layers (tag >= 3)
fixmask = [a.tag >= 3 for a in slab]
slab.set_constraint(FixAtoms(mask=fixmask))

# Set calculator
slab.calc = EMT()

# Save coordinates of fixed atoms before optimization
fixed_indices = [i for i, fix in enumerate(fixmask) if fix]
initial_pos = slab.positions[fixed_indices].copy()

# Optimize
BFGS(slab).run(fmax=0.05)

# Get final positions of fixed atoms
final_pos = slab.positions[fixed_indices]

# Print comparison
print("Fixed atom indices:", fixed_indices)
print("Initial positions (Å):")
print(initial_pos)
print("Final positions (Å):")
print(final_pos)
print("Differences (Å):")
print(final_pos - initial_pos)
max_diff = np.max(np.abs(final_pos - initial_pos))
print(f"Max coordinate change: {max_diff:.6f} Å")
if max_diff < 1e-6:
    print("Fixed atoms did not move (within numerical precision).")
else:
    print("Fixed atoms moved slightly (possible due to EMT noise or constraint tolerance).")
