from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import PreconLBFGS
from ase.lattice.cubic import FaceCenteredCubic
from ase.units import Bohr
import numpy as np

# Create Ni FCC bulk
a = 3.52  # Ni lattice constant in Bohr
atoms = FaceCenteredCubic('Ni', latticeconstant=a)

# Set the EMT calculator with automatic preconditioning
atoms.calc = EMT(precon='auto')

# Perform optimization using PreconLBFGS
optimizer = PreconLBFGS(atoms, trajectory='opt.traj')
optimizer.run(fmax=0.01)

# Retrieve final optimization details
final_energy = atoms.get_potential_energy()
final_cell = atoms.get_cell()

# Number of optimization steps
steps = optimizer.get_nsteps()

# Print results
print(f"Number of steps: {steps}")
print(f"Final energy: {final_energy:.6f} eV")
print("Final cell parameters (in Bohr):")
print(np.squeeze(final_cell))
