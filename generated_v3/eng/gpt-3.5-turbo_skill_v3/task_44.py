from ase.build import fcc111, add_adsorbate
from ase.constraints import FixAtoms
from ase.optimize import BFGS
from ase.calculators.emt import EMT

# Create Cu(111) 4-layer slab
slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0)

# Fix the bottom 2 layers based on tags
slab.set_tags([0, 0, 1, 1])  # Tag 0 for fixed atoms, Tag 1 for free atoms
slab.set_constraint(FixAtoms(mask=[atom.tag == 0 for atom in slab]))

# Add adsorbate for more realistic optimization
add_adsorbate(slab, 'Au', 1.5, position='ontop')

# Set calculator and run BFGS optimization
slab.calc = EMT()
opt = BFGS(slab)
opt.run(fmax=0.05)

# Get the atomic positions of the fixed atoms before and after optimization
fixed_atoms_before = slab[[atom.index for atom in slab if atom.tag == 0]].get_positions()
fixed_atoms_after = opt.atoms[[atom.index for atom in opt.atoms if atom.tag == 0]].get_positions()

# Compare and print the coordinates of fixed atoms before and after optimization
print("Fixed atoms coordinates before optimization:")
print(fixed_atoms_before)

print("\nFixed atoms coordinates after optimization:")
print(fixed_atoms_after)
