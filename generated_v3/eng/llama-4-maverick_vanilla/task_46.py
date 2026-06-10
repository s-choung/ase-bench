from ase import Atoms
from ase.build import fcc111
from ase.constraints import FixAtoms, FixBondLength
from ase.optimize import BFGS
from ase.calculators.emt import EMT

slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)
slab.pbc = True

co = Atoms('CO', positions=[(0, 0, 0), (0, 0, 1.2)])
co.translate((1, 1, 8))

slab.extend(co)

constraint1 = FixAtoms(indices=[i for i, atom in enumerate(slab) if atom.symbol == 'Pt' and atom.z < slab.positions[:, 2].min() + 2.5])
constraint2 = FixBondLength(3, 4)

slab.set_constraint([constraint1, constraint2])
slab.calc = EMT()

opt = BFGS(slab)
opt.run(fmax=0.05)

print(slab.get_potential_energy())
print(slab.get_distance(3, 4))
