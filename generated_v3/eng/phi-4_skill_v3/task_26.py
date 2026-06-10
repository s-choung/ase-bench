from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize.precon import PreconLBFGS
from ase.constraints import FixedCell
import numpy as np

# Build Ni FCC bulk structure
atoms = bulk('Ni', 'fcc', a=3.5)

# Set EMT calculator with precon='auto'
atoms.calc = EMT(precon='auto')

# Constrain cell sizes and angles to use preconferences better
atoms.set_constraint(FixedCell(atoms.get_cell()))

# Set up the PreconLBFGS optimizer
opt = PreconLBFGS(atoms, trajectory='Ni.opt.traj')

# Run optimization
opt.run(fmax=0.01)

# Print results
print(f"Number of steps: {opt.get_number_of_steps()}")
print(f"Final energy: {atoms.get_potential_energy()} eV")
print(f"Final cell parameters: {atoms.get_cell_lengths_and_angles()} Å and degrees")
