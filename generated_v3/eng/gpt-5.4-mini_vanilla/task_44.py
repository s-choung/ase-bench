from ase.build import fcc111
from ase.constraints import FixAtoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.io import write

slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0, orthogonal=True)
slab.calc = EMT()

fixed = [atom.index for atom in slab if atom.tag <= 2]
slab.set_constraint(FixAtoms(indices=fixed))

before = slab.get_positions()[fixed].copy()

opt = BFGS(slab, logfile=None)
opt.run(fmax=0.01)

after = slab.get_positions()[fixed].copy()

print("Fixed atom positions before optimization:")
print(before)
print("\nFixed atom positions after optimization:")
print(after)
print("\nMax displacement of fixed atoms:",
      ((after - before) ** 2).sum(axis=1).max() ** 0.5)
