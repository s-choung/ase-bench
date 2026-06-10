from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.thermochemistry import IdealGasThermo
from ase.md.verlet import VelocityVerlet
from ase import units
import numpy as np

# Create Pd FCC bulk structure
pd_fcc = bulk('Pd', 'fcc', a=3.9)

# Build a 2x2x2 supercell
atoms = pd_fcc.repeat(2)

# Set up EMT calculator
atoms.calc = EMT()

# Relax the structure slightly to get a low-energy configuration
BFGS(atoms).run(fmax=0.001)

# Set initial temperature
ideal = IdealGasThermo(atoms, temp=500, units='K')
atoms.calc.trajectory = None  # Clear any previous trajectory to avoid conflicts
maxwell = MaxwellBoltzmannDistribution(atoms, temperature_K=500)
stationary = Stationary(atoms)
stationary.run()

# Initialize VelocityVerlet MD
md = VelocityVerlet(atoms, timestep=2 * units.fs)

# Perform NVE MD for 200 steps
md.run(nsteps=200)

# Calculate total energy at the start and end
initial_energy = atoms.get_potential_energy() + atoms.get_kinetic_energy()
final_energy = atoms.get_potential_energy() + atoms.get_kinetic_energy()
energy_difference = final_energy - initial_energy

# Print the energy difference
print(f"Energy difference (initial - final): {energy_difference:.6f} eV")
