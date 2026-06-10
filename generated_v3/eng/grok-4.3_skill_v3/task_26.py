from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize.precon import PreconLBFGS
from ase.filters import FrechetCellFilter
atoms = bulk('Ni', 'fcc', a=3.5)
atoms.calc = EMT()
opt = PreconLBFGS(FrechetCellFilter(atoms), precon='auto')
opt.run(fmax=0.01)
print(opt.nsteps, atoms.get_potential_energy(), atoms.get_cell_lengths_and_angles())
