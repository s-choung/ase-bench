from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase import units
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

# Create Pd FCC 2x2x2 supercell
atoms = bulk('Pd', 'fcc', cubic=True) * (2, 2, 2)
atoms.calc = EMT()

# Set initial velocities (500K) and remove COM motion
MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

# Store initial total energy
initial_energy = atoms.get_total_energy()

# Set up and run VelocityVerlet NVE MD for 200 steps
md = VelocityVerlet(atoms, timestep=2 * units.fs)
md.run(200)

# Calculate and print energy difference
final_energy = atoms.get_total_energy()
energy_diff = final_energy - initial_energy
print(f"Energy difference (start to end): {energy_diff:.3f} eV")
