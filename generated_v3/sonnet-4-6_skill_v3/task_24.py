from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import LBFGS
from ase.filters import FrechetCellFilter

atoms = bulk('Au', 'fcc', a=4.08, cubic=True)
atoms.calc = EMT()

filt = FrechetCellFilter(atoms)
opt = LBFGS(filt)
opt.run(fmax=0.01)

print(f"Optimization steps: {opt.nsteps}")
print(f"Final energy: {atoms.get_potential_energy():.6f} eV")
