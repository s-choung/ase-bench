from ase.build import bulk
from ase.calculators.emt import EMT
from ase.filters import FrechetCellFilter
from ase.optimize import LBFGS

# Create Au FCC bulk with a reasonable starting lattice constant
atoms = bulk('Au', 'fcc', a=4.08)
atoms.calc = EMT()

# Optimize both atomic positions and cell using LBFGS
opt = LBFGS(FrechetCellFilter(atoms))
opt.run(fmax=0.01)

# Output requested results
print(f"Number of optimization steps: {opt.nsteps}")
print(f"Final energy: {atoms.get_potential_energy():.6f} eV")
