from ase.build import fcc111
from ase.constraints import FixAtoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# Create Cu(111) slab with 4 layers
slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0)

# Assign tags to layers (ASE automatically assigns tags 1, 2, 3, 4 for each layer)
for i, atom in enumerate(slab):
    atom.tag = (i // 4) + 1

# Fix bottom 2 layers (tags 1 and 2)
constraint = FixAtoms(mask=[atom.tag <= 2 for atom in slab])
slab.set_constraint(constraint)

# Set EMT calculator and run BFGS optimization
slab.calc = EMT()
dyn = BFGS(slab, trajectory='opt.traj')
dyn.run(fmax=0.05)

# Collect and print fixed atoms coordinates
fixed_indices = [i for i, atom in enumerate(slab) if atom.tag <= 2]
print("Fixed atoms before optimization:")
for idx in fixed_indices:
    print(f"Atom {idx}: {slab[idx].position}")

# Reload initial positions from trajectory
slab = dyn.trajectory[-1]  # Final step after optimization

print("\nFixed atoms after optimization:")
for idx in fixed_indices:
    print(f"Atom {idx}: {slab[idx].position}")
