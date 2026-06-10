from ase import Atoms
from ase.lattice import bulk
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.verlet import VelocityVerlet
from ase import units

# Create Pd FCC 2x2x2 supercell
pd = bulk('Pd', 'fcc', a=3.89)
system = pd * (2, 2, 2)

# Set up EMT calculator
system.set_calculator(EMT())

# Initialize velocities for 500K temperature
MaxwellBoltzmannDistribution(system, temperature_K=500)

# Create MD driver
md = VelocityVerlet(system, timestep=2.0 * units.fs)

# Function to get total energy
def get_total_energy():
    return system.get_potential_energy() + system.get_kinetic_energy()

# Store initial energy
initial_energy = get_total_energy()

# Run MD for 200 steps
md.run(200)

# Get final energy
final_energy = get_total_energy()

# Print energy difference
energy_diff = final_energy - initial_energy
print(f"Energy difference after 200 steps: {energy_diff:.6f} eV")
