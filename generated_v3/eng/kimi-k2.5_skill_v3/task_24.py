from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import LBFGS
from ase.filters import FrechetCellFilter

atoms = bulk('Au', 'fcc', a=4.0)
atoms.calc = EMT()
opt = LBFGS(FrechetCellFilter(atoms))
nsteps = opt.run(fmax=0.01)
print(f"Steps: {nsteps}")
print(f"Final energy: {atoms.get_potential_energy():.6f} eV")
