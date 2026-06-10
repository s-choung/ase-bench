from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import LBFGS
from ase.filters import FrechetCellFilter

atoms = bulk('Au', 'fcc', a=3.6)
atoms.calc = EMT()

opt = LBFGS(FrechetCellFilter(atoms), trajectory='au_opt.traj')
opt.run(fmax=0.01)

print(f"Optimization steps: {opt.get_number_of_steps()}")
print(f"Final energy: {atoms.get_potential_energy():.6f} eV")
