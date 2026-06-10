from ase.build import bulk
from ase.calculators.emt import EMT
from ase.filters import FrechetCellFilter
from ase.optimize import BFGS

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

print(f"Before: cell={atoms.cell.lengths()}, E={atoms.get_potential_energy():.4f} eV")

opt = BFGS(FrechetCellFilter(atoms))
opt.run(fmax=0.01)

print(f"After:  cell={atoms.cell.lengths()}, E={atoms.get_potential_energy():.4f} eV")
