from ase.build import fcc111, add_adsorbate, molecule
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms, FixBondLength
from ase.optimize import BFGS

slab = fcc111('Pt', size=(3, 3, 3), vacuum=10.0)
co = molecule('CO')
add_adsorbate(slab, co, height=1.85, position='ontop')

z = slab.positions[:, 2]
bottom = z < z.min() + 1.0
i_c = len(slab) - 2
i_o = len(slab) - 1

slab.set_constraint([
    FixAtoms(indices=[i for i, m in enumerate(bottom) if m]),
    FixBondLength(i_c, i_o)
])

slab.calc = EMT()
opt = BFGS(slab, logfile=None)
opt.run(fmax=0.05)

energy = slab.get_potential_energy()
co_dist = slab.get_distance(i_c, i_o)

print(energy)
print(co_dist)
