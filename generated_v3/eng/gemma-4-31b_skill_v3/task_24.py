from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import LBFGS
from ase.filters import FrechetCellFilter

atoms = bulk('Au', 'fcc', a=4.08)
atoms.calc = EMT()

# Wrap atoms in FrechetCellFilter to optimize both cell and positions
opt = LBFGS(FrechetCellFilter(atoms))
opt.run(fmax=0.01)

print(f"Optimization steps: {opt.nsteps}")
print(f"Final energy: {atoms.get_potential_energy():.4f} eV")
