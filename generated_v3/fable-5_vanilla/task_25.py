from ase.build import bulk
from ase.calculators.emt import EMT
from ase.filters import FrechetCellFilter
from ase.optimize import BFGS

atoms = bulk("Cu", "fcc", a=3.7)
atoms.calc = EMT()

print("Before:")
print("Cell:\n", atoms.cell)
print("Energy:", atoms.get_potential_energy())

opt = BFGS(FrechetCellFilter(atoms))
opt.run(fmax=0.01)

print("After:")
print("Cell:\n", atoms.cell)
print("Energy:", atoms.get_potential_energy())
print("Lattice constant a =", atoms.cell.cellpar()[0] * 2**0.5)
