from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import LBFGS

# Create FCC bulk Au structure
atoms = bulk("Au", crystalstructure="fcc", a=4.08)

# Set up EMT calculator
atoms.calc = EMT()

# Optimize the structure with LBFGS
opt = LBFGS(atoms, trajectory=None)
opt.run(fmax=0.01)

print("Number of optimization steps:", opt.get_number_of_steps())
print("Final energy:", atoms.get_potential_energy())
