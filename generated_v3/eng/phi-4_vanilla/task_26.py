from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import PreconLBFGS
from ase.build import bulk

# Create a Ni FCC bulk structure
ni_fcc = bulk('Ni', 'fcc', a=3.52, size=(2, 2, 2))

# Set up the EMT calculator with precon='auto'
ni_calc = EMT(precon='auto')
ni_fcc.set_calculator(ni_calc)

# Define optimization with convergence criteria
opt = PreconLBFGS(ni_fcc, target=4, fmax=0.01)

# Run the optimization
opt.run(fmax=0.01)

# Print the results
print(f"Number of steps: {opt.get_number_of_steps()}")
print(f"Final energy: {opt.get_potential_energy():.6f}")
print(f"Final cell parameters: {ni_fcc.get_cell()}")
