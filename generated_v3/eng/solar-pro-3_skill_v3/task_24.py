from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter

# Build gold bulk in fcc
atoms = bulk('Au', 'fcc', a=4.0)          # lattice constant in Å
atoms.calc = EMT()

# Optimize cell and atomic positions with Frechet filter
opt = BFGS(FrechetCellFilter(atoms))
opt.run(fmax=0.01)

print(f"Steps: {opt.energy.shape[0]}")
print(f"Final energy (eV): {atoms.get_potential_energy():.6f}")
