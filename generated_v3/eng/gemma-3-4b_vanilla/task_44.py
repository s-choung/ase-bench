from ase.build import fcc111, add_adsorbate
from ase.calculators import EMT, LJ
from ase.constraints import FixAtoms
from ase.optimize import BFGS
from ase.io import write

# Build a Cu(111) 4-layer slab
slab = fcc111('Cu', size=(3, 3, 4), vacuum=1.0)

# Add a single hydrogen atom as an adsorbate
add_adsorbate(slab, 'H', height=2.0)

# Set tags for the bottom 2 layers
tags = ['bottom_layer_1', 'bottom_layer_2']
for tag in tags:
    slab.tag(tag)

# Constraint the bottom 2 layers
constraint = FixAtoms(tags=tags)
slab.set_constraint(constraint)

# Calculate using EMT
calc = EMT()
slab.calc = calc

# Structural optimization using BFGS
dyn = BFGS(slab, trajectory='optimization.traj')
dyn.run(fmax=0.01)

# Print coordinates before and after optimization
print("Before optimization:")
for atom in slab:
    print(f"Atom {atom.tag}: {atom.position}")

print("\nAfter optimization:")
for atom in slab:
    print(f"Atom {atom.tag}: {atom.position}")

# Write the optimized structure to a file
write('optimized_slab.xyz', slab)
