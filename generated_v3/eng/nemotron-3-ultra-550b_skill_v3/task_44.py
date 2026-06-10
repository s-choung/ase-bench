from ase.build import fcc111
from ase.constraints import FixAtoms
from ase.optimize import BFGS
from ase.calculators.emt import EMT

slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0)
fixed_indices = [i for i, atom in enumerate(slab) if atom.tag <= 2]
initial_positions = slab.get_positions()[fixed_indices].copy()

slab.set_constraint(FixAtoms(indices=fixed_indices))
slab.calc = EMT()
BFGS(slab).run(fmax=0.05)

final_positions = slab.get_positions()[fixed_indices]
print("Fixed atom coordinates comparison (initial vs final):")
for i, (init, final) in enumerate(zip(initial_positions, final_positions)):
    diff = final - init
    print(f"Atom {fixed_indices[i]}: init={init}, final={final}, diff={diff}, max|diff|={abs(diff).max():.2e}")
