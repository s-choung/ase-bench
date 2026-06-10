from ase.build import fcc111
from ase.constraints import FixAtoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# Create 4-layer Cu(111) slab
slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0)

# Fix bottom 2 layers (tags 0 and 1)
constraint = FixAtoms(indices=[atom.index for atom in slab if atom.tag < 2])
slab.set_constraint(constraint)

# Store original positions of fixed atoms
fixed_indices = [atom.index for atom in slab if atom.tag < 2]
original_positions = slab.get_positions()[fixed_indices].copy()

# Set calculator and optimize
slab.calc = EMT()
opt = BFGS(slab, trajectory='opt.traj')
opt.run(fmax=0.05, steps=100)

# Get final positions of fixed atoms
final_positions = slab.get_positions()[fixed_indices]

# Print comparison
print("Fixed atoms coordinates before optimization:")
print(original_positions)
print("\nFixed atoms coordinates after optimization:")
print(final_positions)
print("\nMaximum displacement of fixed atoms:")
print(max(abs(original_positions - final_positions).flatten()))
