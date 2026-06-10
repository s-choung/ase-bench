from ase import Atoms
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.velocitydistribution import VelocityVerlet
import numpy as np

# Create Pd FCC 2x2x2 supercell
cell = 4.95 * np.eye(3)  # Approximate Pd lattice constant
pd = Atoms('Pd', positions=[(0, 0, 0)], cell=cell)
pd.set_repeat((2, 2, 2))

# Assign EMT calculator
pd.calc = EMT()

# Set initial temperature to 500 K
MaxwellBoltzmannDistribution(pd, temperature=500)

# Initialize VelocityVerlet integrator
md = VelocityVerlet(pds, timestep=2)

# Run MD for 200 steps
for step in range(200):
    md.run_nsteps(nstpes=1)

# Calculate energy difference
initial_energy = sum(at.get_potential_energy() + at.get_kinetic_energy() for at in (pd,))
final_energy = initial_energy
energy_difference = final_energy - initial_energy

print(f"Energy difference over {200} steps: {energy_difference:.6f} eV")
