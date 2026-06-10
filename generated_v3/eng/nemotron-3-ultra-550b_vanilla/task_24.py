from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import LBFGS

# Create Au FCC bulk
atoms = bulk('Au', 'fcc', a=4.05)
atoms.calc = EMT()

# Optimize
opt = LBFGS(atoms, logfile='-')
opt.run(fmax=0.01)

# Print results
print(f"Optimization steps: {opt.nsteps}")
print(f"Final energy: {atoms.get_potential_energy():.6f} eV")
