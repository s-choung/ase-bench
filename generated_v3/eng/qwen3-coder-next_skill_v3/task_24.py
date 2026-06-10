from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import LBFGS

# Create FCC Au bulk structure
atoms = bulk('Au', 'fcc', a=4.08)
atoms.calc = EMT()

# Optimize with LBFGS
opt = LBFGS(atoms)
opt.run(fmax=0.01)

# Print results
print(f"Optimization steps: {len(opt trajectory) - 1}")
print(f"Final energy: {atoms.get_potential_energy():.6f} eV")
