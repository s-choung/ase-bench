from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import LBFGS

# Create FCC Au bulk structure
atoms = bulk('Au', crystalstructure='fcc', a=4.08)

# Set up EMT calculator
atoms.calc = EMT()

# Optimize with LBFGS
opt = LBFGS(atoms, trajectory=None)
opt.run(fmax=0.01)

# Print results
print(f"Optimization steps: {opt.get_number_of_steps()}")
print(f"Final energy: {atoms.get_potential_energy():.4f} eV")
