from ase.build import fcc111, add_adsorbate
from ase.constraints import FixAtoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS

slab = fcc111('Cu', size=(3, 3, 4), vacuum=10.0)

# Fix bottom 2 layers
mask = [atom.tag > 2 for atom in slab]
slab.set_constraint(FixAtoms(mask=mask))

slab.set_calculator(EMT())
opt = BFGS(slab)
opt.run(fmax=0.01)

# Print coordinates of fixed atoms before and after optimization
fixed_before = slab.constraints[0].index
fixed_atoms_before = slab.positions[fixed_before]

opt.update()
fixed_atoms_after = slab.positions[fixed_before]

print(f"Coordinates of fixed atoms before optimization:\n{fixed_atoms_before}")
print(f"Coordinates of fixed atoms after optimization:\n{fixed_atoms_after}")
