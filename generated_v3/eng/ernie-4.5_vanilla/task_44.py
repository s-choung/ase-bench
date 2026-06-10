from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS

# Create a 4-layer Cu(111) slab
slab = fcc111('Cu', size=(1, 1, 4), vacuum=10.0)

# Tag the bottom 2 layers for fixing
for atom in slab[:2*len(slab)//4]:  # First two layers
    atom.tag = 1

# Apply constraint based on tags
constraint = FixAtoms(mask=[atom.tag == 1 for atom in slab])
slab.set_constraint(constraint)

# Print coordinates of fixed atoms before optimization
print("Coordinates before optimization:")
for atom in slab:
    if atom.tag == 1:
        print(atom.index, atom.position)

# Set up calculator and optimizer
slab.set_calculator(EMT())
opt = BFGS(slab, trajectory=None)  # No trajectory file
opt.run(fmax=0.01)

# Print coordinates of fixed atoms after optimization
print("\nCoordinates after optimization:")
for atom in slab:
    if atom.tag == 1:
        print(atom.index, atom.position)
