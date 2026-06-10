from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.verlet import VelocityVerlet
import numpy as np

# Create Pd FCC 2x2x2 supercell
atoms = bulk('Pd', 'fcc', a=3.93, cubic=True).repeat((2,2,2))
atoms.calc = EMT()

# Set initial temperature to 500K
MaxwellBoltzmannDistribution(atoms, temperature_K=500, force_temp=True)

# Store initial total energy
initial_energy = atoms.get_total_energy()

# Run VelocityVerlet NVE MD for 200 steps
dyn = VelocityVerlet(atoms, timestep=2.0)
dyn.run(200)

# Calculate and print energy difference
final_energy = atoms.get_total_energy()
print(f"Energy difference (end - start): {final_energy - initial_energy:.6f} eV")
