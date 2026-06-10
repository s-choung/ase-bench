from ase.build import bulk
from ase.calculators.emt import EMT
from ase.filters import ExpCellFilter
from ase.optimize import LBFGS

atoms = bulk('Au', 'fcc', a=4.0)
atoms.calc = EMT()
opt = LBFGS(ExpCellFilter(atoms))
opt.run(fmax=0.01)
print(f'Steps: {opt.steps}')
print(f'Energy: {atoms.get_potential_energy():.4f} eV')
