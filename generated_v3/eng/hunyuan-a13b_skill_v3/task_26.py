from ase import Atoms
from ase.cell import Cell
from ase import bulk
from ase.calculators.emt import EMT
from ase.optimize import PreconLBFGS

# Create Ni FCC bulk
atoms = bulk('Ni', 'fcc', a=3.5, cubic=True)

# Set up PreconLBFGS optimizer with EMT and precon='auto'
atoms.calc = EMT()
opt = PreconLBFGS(atoms, precon='auto', fmax=0.01)

# Run optimization
opt.run()

# Print results
print(f"Steps: {opt.nsteps}")
print(f"Final Energy: {opt.e_final} Hartree")
print(f"Cell Parameters: {atoms.cell}")
