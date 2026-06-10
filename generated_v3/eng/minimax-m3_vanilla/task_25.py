from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

a0 = atoms.cell[0, 0]
e0 = atoms.get_potential_energy()
print(f"Before: a={a0:.4f}, E={e0:.4f}")

opt = BFGS(FrechetCellFilter(atoms), logfile=None)
opt.run(fmax=0.01)

a1 = atoms.cell[0, 0]
e1 = atoms.get_potential_energy()
print(f"After:  a={a1:.4f}, E={e1:.4f}")
