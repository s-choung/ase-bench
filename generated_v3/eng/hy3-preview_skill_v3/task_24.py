from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import LBFGS

# Create Au FCC bulk structure
atoms = bulk('Au', 'fcc', a=4.08)

# Set calculator
atoms.calc = EMT()

# Optimize using LBFGS
opt = LBFGS(atoms, trajectory=None, logfile=None)
steps = opt.run(fmax=0.01)

# Print results
print(f"Optimization steps: {opt.nsteps}")
print(f"Final energy: {atoms.get_potential_energy():.6f} eV")
