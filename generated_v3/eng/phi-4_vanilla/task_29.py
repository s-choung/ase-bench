from ase import Atoms
from ase.build import bulk
from ase.calculators.lj import LennardJones
from ase.calculators.emt import EMT
from ase.md.velocityverlet import VelocityVerlet
import numpy as np

# Create Pd FCC 2x2x2 supercell
pd2 = bulk('Pd', 'fcc', a=4.01)
pd2 = pd2.repeat((2, 2, 2))

# Set calculator
calculator = EMT()

# Attach calculator to the system
pd2.set_calculator(calculator)

# Set the initial temperature
pd2.set_temperature(500)

# Perform a quick minimization to relax to a stable state
import ase.calculators.eam as eam
pd2.set_calculator(eam.EAM(list_pd='pd.eam.alloy'))
pd2.get_potential_energy()

# Initialize Verlet integrator
nvt = VelocityVerlet(pd2, t=0, dt=2, tlims=6000)

# Run MD
nvt.run(steps=200)

# After MD, attach EMT calculator again to get potential energy
pd2.set_calculator(calculator)

# Calculate kinetic and potential energy at the end
final_energy = pd2.get_potential_energy()
final_energy += nvt.get_temperature() * pd2.get_kinetic_energy()

# Print energy difference
print(f"Energy difference: {final_energy - pd2.get_potential_energy() - nvt.get_temperature() * pd2.get_kinetic_energy():.3f} eV")
