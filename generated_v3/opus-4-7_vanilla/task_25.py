from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

print("Before optimization")
print("Cell:", atoms.cell.lengths())
print("Energy:", atoms.get_potential_energy())

ecf = FrechetCellFilter(atoms)
opt = BFGS(ecf)
opt.run(fmax=0.01)

print("After optimization")
print("Cell:", atoms.cell.lengths())
print("Energy:", atoms.get_potential_energy())
