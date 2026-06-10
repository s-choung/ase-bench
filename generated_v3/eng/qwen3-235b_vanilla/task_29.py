from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md import VelocityVerlet
from ase.units import fs, kB

# Create Pd FCC 2x2x2 supercell
atoms = bulk('Pd', cubic=True) * (2, 2, 2)

# Set EMT calculator
atoms.set_calculator(EMT())

# Initialize velocities for 500 K
MaxwellBoltzmannDistribution(atoms, temperature_K=500)

# Get initial total energy
initial_energy = atoms.get_total_energy()

# Run VelocityVerlet dynamics
dyn = VelocityVerlet(atoms, timestep=2*fs)
for _ in range(200):
    dyn.run(1)

# Get final total energy
final_energy = atoms.get_total_energy()

# Print energy difference
print(final_energy - initial_energy)
