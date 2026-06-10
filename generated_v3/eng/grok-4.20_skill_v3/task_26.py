from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize.precon import PreconLBFGS
from ase.filters import FrechetCellFilter
import numpy as np

atoms = bulk('Ni', 'fcc', a=3.52)
atoms.calc = EMT()
opt = PreconLBFGS(FrechetCellFilter(atoms), precon='auto')
opt.run(fmax=0.01)
print(opt.get_number_of_steps())
print(atoms.get_potential_energy())
print(atoms.get_cell_lengths_and_angles()[:6])
