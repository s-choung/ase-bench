from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import LBFGS

# Create Au FCC structure
atoms = bulk('Au', 'fcc', a=4.08)
atoms.calc = EMT()

# Optimize structure
opt = LBFGS(atoms, logfile=None)
opt.run(fmax=0.01)

# Output results
print(f"Steps: {opt.nsteps}")
print(f"Final Energy: {atoms.get_total_energy():.4f} eV")
