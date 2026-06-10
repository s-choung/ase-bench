from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()
print('Before:', atoms.get_cell_lengths_and_angles(), 'Energy:', atoms.get_potential_energy())

opt = BFGS(FrechetCellFilter(atoms))
opt.run(fmax=0.01)

print('After:', atoms.get_cell_lengths_and_angles(), 'Energy:', atoms.get_potential_energy())
