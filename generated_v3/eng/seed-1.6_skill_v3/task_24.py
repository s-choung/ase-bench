from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import LBFGS
from ase.filters import FrechetCellFilter

atoms = bulk('Au', 'fcc')
atoms.calc = EMT()
opt = LBFGS(FrechetCellFilter(atoms))
opt.run(fmax=0.01)
print(f"Steps: {opt.nsteps}, Final energy: {atoms.get_potential_energy():.6f} eV")
