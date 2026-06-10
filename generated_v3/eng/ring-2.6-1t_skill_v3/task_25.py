from ase.build import bulk
from ase.calculators.emt import EMT
from ase.filters import FrechetCellFilter
from ase.optimize import BFGS

atoms = bulk('Cu', 'fcc', a=3.5)
atoms.calc = EMT()

print(f"Before: cell = {atoms.get_cell_lengths_and_angles()[:3]}, energy = {atoms.get_potential_energy():.4f} eV")

opt = BFGS(FrechetCellFilter(atoms))
opt.run(fmax=0.01)

print(f"After:  cell = {atoms.get_cell_lengths_and_angles()[:3]}, energy = {atoms.get_potential_energy():.4f} eV")
