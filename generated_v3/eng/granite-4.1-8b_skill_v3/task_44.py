from ase import Atoms
from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FixAtoms

# Create a Cu(111) slab with 4 layers
slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0)

# Tag the bottom 2 layers
for a in slab:
    if a.position[2] < 0.5 * slab.cell[2, 2]:
        a.tag = 1  # Mark atoms in bottom 2 layers
    else:
        a.tag = 0

# Apply FixAtoms constraint to keep the bottom 2 layers fixed
constraints = FixAtoms(mask=[tag == 1 for tag in slab.tag])

# Set the EMT calculator
slab.calc = EMT()

# Apply constraints
slab.set_constraint(constraints)

# Perform BFGS optimization
opt = BFGS(slab)
opt.run(fmax=0.05)

# Gather and print fixed atom coordinates before and after optimization
print("Fixed atoms coordinates before optimization:")
for a in slab:
    if a.tag == 1:
        print(f"{a.position[0]:.6f} {a.position[1]:.6f} {a.position[2]:.6f}")

slab.calc.results.pop()  # Clear previous calculations

# Recalculate to get updated positions after optimization
slab.calc = EMT()
slab.get_potential_energy()
opt = BFGS(slab)
opt.run(fmax=0.05)

print("\nFixed atoms coordinates after optimization:")
for a in slab:
    if a.tag == 1:
        print(f"{a.position[0]:.6f} {a.position[1]:.6f} {a.position[2]:.6f}")
