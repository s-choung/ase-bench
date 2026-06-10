from ase.build import fcc111, make_cubic
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FixAtoms

slab = fcc111('Cu', size=(4, 4, 4), vacuum=5.0)
calc = EMT()
slab.calc = calc

tags = [atom.tag for atom in slab if atom.z < 2 * slab.cell[2, 2]]
constraint = FixAtoms(mask=tags)
slab.set_constraint(constraint)

initial_fixed_coords = slab.get_positions(tags=tags)

slab.optimize(method='BFGS')

final_fixed_coords = slab.get_positions(tags=tags)

print("Initial fixed atom coordinates:")
print(initial_fixed_coords)
print("\nFinal fixed atom coordinates:")
print(final_fixed_coords)
