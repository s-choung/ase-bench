from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import PreconLBFGS
from ase.visualize import view

# Create a bulk Ni FCC structure
atoms = bulk('Ni', 'fcc', a=3.58)
atoms.calc = EMT(concenter='Vosko-Wilk') # Use Vosko-Wilk for better convergence
# Perform optimization using PreconLBFGS
opt = PreconLBFGS(atoms, precon='auto')
opt.run(fmax=0.01, steps=1000)

# Print the results
print("Number of steps:", opt.fortSteps)
print("Final energy:", atoms.get_potential_energy())
print("Cell parameters:", atoms.get_cell())

# Visualize the optimized structure
view(atoms)
