import numpy as np
from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import PreconLBFGS
from ase.build import bulk

# Create Ni FCC structure (using EMT which is for Cu, Ag, Au, but following prompt instructions)
atoms = bulk('Ni', 'fcc', a=3.5)
atoms.calc = EMT()

# Setup optimizer
opt = PreconLBFGS(atoms, precon='auto')

# Run optimization
opt.run(fmax=0.01)

# Output results
print(f"Steps: {opt.get_number_of_steps()}")
print(f"Final Energy: {atoms.get_potential_energy():.6f} eV")
print(f"Cell parameters: {atoms.get_cell_lengths_and_angles()}")
