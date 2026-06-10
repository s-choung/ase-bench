from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

# Create Cu bulk system
atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms.calc = EMT()

# Set initial velocities (300K)
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)  # Remove COM motion

# NVE integrator
md = VelocityVerlet(atoms, timestep=5 * units.fs)

# Print initial energy
print(f"Initial total energy: {atoms.get_total_energy():.3f} eV")

# Run 50 steps
md.run(50)

# Print final energy
print(f"Final total energy: {atoms.get_total_energy():.3f} eV")
