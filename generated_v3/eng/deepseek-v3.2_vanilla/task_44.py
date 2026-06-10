from ase import Atoms
from ase.build import fcc111, add_adsorbate
from ase.constraints import FixAtoms
from ase.optimize import BFGS
from ase.calculators.emt import EMT

slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0)
slab.center()

tags = slab.get_tags()
tags[8:] = [1, 1, 1, 1]
tags[:8] = [0, 0, 0, 0]
slab.set_tags(tags)

mask = [tag == 0 for tag in slab.get_tags()]
constraint = FixAtoms(mask=mask)
slab.set_constraint(constraint)

initial_positions = slab.get_positions()[mask].copy()

slab.calc = EMT()
opt = BFGS(slab)
opt.run(fmax=0.05)

final_positions = slab.get_positions()[mask]

print("Fixed atom coordinates comparison:")
print(f"{'Atom':<6} {'Initial X':<12} {'Final X':<12} {'Delta X':<12}")
print("-" * 60)
for i in range(len(initial_positions)):
    dx = final_positions[i, 0] - initial_positions[i, 0]
    print(f"{i:<6} {initial_positions[i, 0]:<12.6f} {final_positions[i, 0]:<12.6f} {dx:<12.6f}")
