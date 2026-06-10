from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS

atoms = fcc111('Cu', size=(1, 1, 4), vacuum=10.0)
mask = [a.tag >= 3 for a in atoms]
fixed = [i for i, m in enumerate(mask) if m]
before = atoms.positions[fixed].copy()

atoms.set_constraint(FixAtoms(mask=mask))
atoms.calc = EMT()
BFGS(atoms).run(fmax=0.05)

after = atoms.positions[fixed]
print('Before:')
print(before)
print('After:')
print(after)
print('Max displacement (Å):', abs(after - before).max())
