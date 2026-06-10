from ase import units
from ase.build import fcc111
from ase.constraints import FixAtoms
from ase.optimize import BFGS
from ase.calculators.emt import EMT

slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0)
slab.calc = EMT()
fixed_mask = [a.tag <= 2 for a in slab]
slab.set_constraint(FixAtoms(mask=fixed_mask))
initial_pos = slab.positions.copy()
BFGS(slab).run(fmax=0.05)
for i, (fixed, old, new) in enumerate(zip(fixed_mask, initial_pos, slab.positions)):
    if fixed:
        print(f"Atom {i}: initial={old} final={new}")
