from ase.build import bulk
from ase.calculators.emt import EMT
from ase.filters import FrechetCellFilter
from ase.optimize import BFGS

atoms = bulk('Cu', 'fcc', a=3.5, cubic=True)
atoms.calc = EMT()

print("Before:")
print("Cell:\n", atoms.get_cell())
print("Energy:", atoms.get_potential_energy(), "eV")

opt = BFGS(FrechetCellFilter(atoms))
opt.run(fmax=0.01)

print("\nAfter:")
print("Cell:\n", atoms.get_cell())
print("Lattice constant a =", atoms.get_cell_lengths_and_angles()[0], "Å")
print("Energy:", atoms.get_potential_energy(), "eV")
