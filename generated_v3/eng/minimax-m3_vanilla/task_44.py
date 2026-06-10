from ase.build import fcc111
from ase.constraints import FixAtoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# Build Cu(111) slab, 4 layers, 2x2 in-plane
slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0)

# Tag bottom 2 layers -> 0 (fixed), top 2 layers -> 1 (free)
z_levels = sorted(set(slab.get_positions()[:, 2].round(decimals=4)))
z_mid = 0.5 * (z_levels[1] + z_levels[2])
slab.set_tags([0 if z < z_mid else 1 for z in slab.get_positions()[:, 2]])

# Constrain fixed atoms via tags
slab.set_constraint(FixAtoms(mask=slab.get_tags() == 0))

# Snapshot fixed-atom positions BEFORE optimization
fixed_mask = slab.get_tags() == 0
pos_before = slab.get_positions()[fixed_mask].copy()

# Run BFGS with EMT
slab.calc = EMT()
BFGS(slab, logfile=None).run(fmax=0.05)

# Snapshot fixed-atom positions AFTER optimization
pos_after = slab.get_positions()[fixed_mask]
disps = ((pos_after - pos_before) ** 2).sum(axis=1) ** 0.5

# Print comparison
print("Fixed-atom coordinates (BEFORE -> AFTER BFGS):")
for i, (b, a, d) in enumerate(zip(pos_before, pos_after, disps)):
    print(f"  {i:2d}: ({b[0]: .6f}, {b[1]: .6f}, {b[2]: .6f}) -> "
          f"({a[0]: .6f}, {a[1]: .6f}, {a[2]: .6f})  |Δ| = {d:.2e} Å")

print(f"\nMax displacement of fixed atoms: {disps.max():.2e} Å")
assert disps.max() < 1e-6, "Fixed atoms moved during optimization!"
print("OK: all fixed atoms remained stationary.")
