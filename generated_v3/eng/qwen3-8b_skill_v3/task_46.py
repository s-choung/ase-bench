import numpy as np
from ase.build import fcc111, molecule, add_adsorbate
from ase.constraints import FixAtoms, FixBondLength
from ase.optimize import BFGS
from ase.calculators.emt import EMT
from ase.geometry import get_distances

slab = fcc111('Pt', size=(1, 1, 3), vacuum=10.0)
original_len = len(slab)
co = molecule('CO')
add_adsorbate(slab, co, height=1.8, position='ontop')

original_positions = slab.get_positions()[:original_len]
min_z = min(p[2] for p in original_positions)
tolerance = 0.5
mask = [a.position[2] < min_z + tolerance for a in slab]

fix_bottom = FixAtoms(mask=mask)
fix_co = FixBondLength(original_len, original_len + 1)
slab.set_constraint([fix_bottom, fix_co])

slab.calc = EMT()
opt = BFGS(slab)
opt.run(fmax=0.05)

print("Final energy:", slab.get_potential_energy())
co_atoms = slab[original_len:original_len+2]
distance = co_atoms[0].distance(co_atoms[1])
print("C-O distance:", distance)
