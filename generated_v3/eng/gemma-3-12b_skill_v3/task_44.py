from ase.build import fcc111
from ase.constraints import FixAtoms
from ase.calculators import EMT
from ase.optimize import BFGS

slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0)
calc = EMT()
slab.calc = calc

# Assign tags to atoms (0 for the top 2 layers, 1 for the bottom 2 layers)
for i, atom in enumerate(slab):
    if atom.position[2] < slab.cell[2, 2] / 2:
        atom.tag = 1
    else:
        atom.tag = 0

# Fix the bottom 2 layers
fix_atoms = FixAtoms(mask=[a.tag == 1 for a in slab])
slab.set_constraint(fix_atoms)

# Print initial coordinates of fixed atoms
print("Initial coordinates of fixed atoms:")
for a in slab:
    if a.tag == 1:
        print(f"Atom {a.index}: {a.position}")

# Optimize the slab
opt = BFGS(slab, trajectory='opt.traj')
opt.run(fmax=0.05)

# Print final coordinates of fixed atoms
print("\nFinal coordinates of fixed atoms:")
for a in slab:
    if a.tag == 1:
        print(f"Atom {a.index}: {a.position}")
