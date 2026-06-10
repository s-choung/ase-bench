from ase.build import fcc111
from ase.constraints import FixAtoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# Build Cu(111) 4-layer slab
slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0)
positions_before = slab.positions.copy()

# Tag the bottom 2 layers
for atom in slab:
    if atom.z < sorted(set(slab.positions[:, 2]))[-2]:
        atom.tag = 1

# Apply constraint to fix the atoms with tag 1
constraint = FixAtoms(indices=[atom.index for atom in slab if atom.tag == 1])
slab.set_constraint(constraint)

# Set EMT calculator
slab.set_calculator(EMT())

# Run BFGS optimization
opt = BFGS(slab)
opt.run(fmax=0.01)

# Check positions after optimization
positions_after = slab.positions
fixed_indices = [atom.index for atom in slab if atom.tag == 1]

print("Fixed atom positions before optimization:")
for i in fixed_indices:
    print(positions_before[i])

print("\nFixed atom positions after optimization:")
for i in fixed_indices:
    print(positions_after[i])
