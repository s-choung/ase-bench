from ase.build import fcc111, molecule
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS

slab = fcc111('Al', size=(2, 2, 3), vacuum=10.0)
n2 = molecule('N2')

slab_center = slab.get_cell().lengths()[0] / 2
slab += n2
n2_idx = [-2, -1]
slab[n2_idx].positions[:, 2] += 2.0

slab[n2_idx[0]].position = [slab_center - 0.5, slab_center, slab.get_positions()[:, 2].max() + 2.0]
slab[n2_idx[1]].position = [slab_center + 0.5, slab_center, slab.get_positions()[:, 2].max() + 2.0]

mask = [atom.symbol == 'Al' and atom.position[2] < slab.get_positions()[:, 2].max() - 1e-6 for atom in slab]
slab.set_constraint(FixAtoms(mask=mask))
slab.calc = EMT()

opt = BFGS(slab, logfile=None)
opt.run(fmax=0.05)

print(len(slab), slab.get_chemical_symbols())
