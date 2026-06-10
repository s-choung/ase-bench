from ase.build import bulk
from ase.calculators.emt import EMT
from ase.constraints import ExpCellFilter
from ase.optimize import LBFGS

atoms = bulk('Au', 'fcc')
atoms.calc = EMT()
opt = LBFGS(ExpCellFilter(atoms))
opt.run(fmax=0.01)
print(f"Optimization steps: {opt.nsteps}")
print(f"Final energy: {atoms.get_potential_energy():.4f} eV")
