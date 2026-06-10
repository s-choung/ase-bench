from ase import Atoms
from ase.build import bulk
from ase.build import fcc111
from ase.optimize import LBFGS
from ase.calculators.emt import EMT

# Create an FCC bulk structure of Gold (Au)
au_fcc = bulk('Au', 'fcc', a=4.08)
au_fcc.set_calculator(EMT())

# Use the Limited-memory BFGS optimizer to optimize the structure
optimizer = LBFGS(au_fcc, trajectory='au_fcc', fmax=0.01)

# Perform the optimization
iau = optimizer.run(fmax=0.01)

# Print the number of optimization steps and final energy
print(f"Optimization took {len(iau)} steps.")
print(f"Final energy: {iau[-1].get_potential_energy()} eV")
