from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS

slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0)
slab.calc = EMT()
fix_layers = 2
fixed_indices = [atom.index for atom in slab if atom.tag <= fix_layers]
initial_positions = slab.get_positions()[fixed_indices].copy()

slab.set_constraint(FixAtoms(indices=fixed_indices))
opt = BFGS(slab)
opt.run(fmax=0.05)

final_positions = slab.get_positions()[fixed_indices]

print("Fixed atoms' initial positions:\n", initial_positions)
print("Fixed atoms' final positions after optimization:\n", final_positions)
assert (initial_positions == final_positions).all(), "Fixed atoms moved!"
