from ase.build import fcc111, add_adsorbate, molecule
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms, FixBondLength
from ase.optimize import BFGS
from ase.geometry import get_distances
import numpy as np

slab = fcc111('Pt', size=(3, 3, 3), vacuum=10.0)
co = molecule('CO')
add_adsorbate(slab, co, height=1.85, position='ontop')

slab.center(axis=2, vacuum=10.0)
slab.calc = EMT()

z = slab.positions[:, 2]
bottom = np.where(z < np.sort(np.unique(np.round(z, 3)))[1])[0]

c_idx = len(slab) - 2
o_idx = len(slab) - 1

slab.set_constraint([
    FixAtoms(indices=bottom),
    FixBondLength(c_idx, o_idx)
])

opt = BFGS(slab, logfile='-')
opt.run(fmax=0.05)

energy = slab.get_potential_energy()
co_dist = slab.get_distance(c_idx, o_idx)

print(f'Final energy: {energy:.6f} eV')
print(f'C-O distance: {co_dist:.6f} Å')
