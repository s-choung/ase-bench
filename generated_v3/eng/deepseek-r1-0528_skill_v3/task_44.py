from ase.build import fcc111
from ase.atoms import Atoms
from ase.constraints import FixAtoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# Build Cu(111) slab with 4 layers
atoms: Atoms = fcc111('Cu', size=(2, 2, 4), vacuum=7.5)

# Tag atoms by layer (0-indexed from bottom)
tags = [a.position[2] for a in atoms]
z_sorted = sorted(set(tags))
for i, atom in enumerate(atoms):
    atoms[i].tag = z_sorted.index(atom.position[2])

# Apply constraint to bottom two layers
mask = [a.tag in [0, 1] for a in atoms]
constraint = FixAtoms(mask=mask)
atoms.set_constraint(constraint)

# Record initial positions of fixed atoms
fixed_indices = [i for i in range(len(atoms)) if mask[i]]
initial_coords = atoms.positions[fixed_indices].copy()

# Run optimization
atoms.calc = EMT()
opt = BFGS(atoms, trajectory='relax.traj')
opt.run(fmax=0.05)

# Record final positions of fixed atoms
final_coords = atoms.positions[fixed_indices]

# Print coords before & after optimization
print("Fixed atom coordinates before relaxation:")
print(initial_coords)
print("\nFixed atom coordinates after relaxation:")
print(final_coords)
print("\nMaximum movement of fixed atoms (Å):", abs(final_coords - initial_coords).max())
