from ase.build import bulk
from ase.calculators.emt import EMT
from ase.filters import FrechetCellFilter
from ase.optimize.precon import PreconLBFGS

atoms = bulk('Ni', 'fcc', a=3.52, cubic=True)
atoms.calc = EMT()

cell_filter = FrechetCellFilter(atoms)
opt = PreconLBFGS(cell_filter, precon='auto')
opt.run(fmax=0.01)

print("steps:", opt.nsteps)
print("final energy (eV):", atoms.get_potential_energy())
print("cell parameters:", atoms.get_cell_lengths_and_angles())
