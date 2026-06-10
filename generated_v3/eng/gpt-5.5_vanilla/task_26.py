from ase.build import bulk
from ase.calculators.emt import EMT
from ase.filters import FrechetCellFilter
from ase.optimize.precon import PreconLBFGS

atoms = bulk("Ni", "fcc", a=3.52, cubic=True)
atoms.calc = EMT()

ecf = FrechetCellFilter(atoms)
opt = PreconLBFGS(ecf, precon="auto", logfile=None)
opt.run(fmax=0.01)

print("steps:", opt.get_number_of_steps())
print("final energy:", atoms.get_potential_energy())
print("cell parameters:", atoms.cell.cellpar())
