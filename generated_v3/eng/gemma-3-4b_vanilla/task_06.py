from ase import Atoms
from ase.md.langevin import Langevin
from ase.calculators import EMT
from ase.build import fcc111
from ase.trajectory import Trajectory
import numpy as np

# Create Cu FCC bulk
a = 3.61  # Å
cell = fcc111(a, colors='grey', size=(2, 2, 2))

# Initialize calculator and atoms
calc = EMT()
atoms = Atoms(cell, calculator=calc)

# Set Langevin parameters
dt = 5.0  # fs
nsteps = 100
temp = 300.0  # K
viscosity = 0.01
zeta = 0.01

# Create Langevin MD object
md = Langevin(atoms, dt=dt, nsteps=nsteps, temp=temp, viscosity=viscosity, zeta=zeta)

# Run MD simulation
md.run()

# Print initial and final temperature and energy
print(f"Initial Temperature: {calc.get_temperature()} K")
print(f"Final Temperature: {calc.get_temperature()} K")
print(f"Initial Energy: {calc.get_potential_energy()} eV")
print(f"Final Energy: {calc.get_potential_energy()} eV")
