from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import LBFGS
from ase.lattice.cubic import FaceCenteredCubic

# Create Au FCC bulk structure
atoms = FaceCenteredCubic(symbol='Au', latticeconstant=4.08, size=(1, 1, 1))

# Set EMT calculator
atoms.calc = EMT()

# Optimize using LBFGS
opt = LBFGS(atoms, fmax=0.01)
opt.run()

# Print results
print(f"Number of optimization steps: {opt.nsteps}")
print(f"Final energy: {atoms.get_potential_energy():.6f} eV")
