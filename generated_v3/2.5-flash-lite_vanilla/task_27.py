from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.npt import NPT
from ase.md.langevin import Langevin
from ase.md.verlet import VelocityVerlet
from ase.constraints import FixAtoms
from ase.io import Trajectory
import numpy as np

# Create Ag FCC 2x2x2 supercell
atoms = fcc111('Ag', size=(2, 2, 2), vacuum=10.0)

# Set EMT calculator
atoms.calc = EMT()

# Set temperature and timestep
T = 500.0  # Kelvin
dt = 5.0  # fs
nsteps = 200

# Initialize velocities from Maxwell-Boltzmann distribution
MaxwellBoltzmannDistribution(atoms, temperature=T)

# Apply constraints to the bottom layer
constraint = FixAtoms(indices=[atom.index for atom in atoms if atom.position[2] < 1.0])
atoms.set_constraint(constraint)

# Use Langevin thermostat for NVT ensemble
thermostat = Langevin(atoms, timestep=dt, temperature_K=T, friction=0.1)

# Run MD simulation
for step in range(nsteps):
    thermostat.step()
    if (step + 1) % 50 == 0:
        print(f"Step: {step + 1}, Temperature: {atoms.get_temperature():.2f} K")
