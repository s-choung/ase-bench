from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.units import fs, Kelvin

# Build Cu 2x2x2 FCC supercell
cu = bulk('Cu', 'fcc').multiply((2,2,2))
cu.calc = EMT()

# Initialize velocities to 300K
MaxwellBoltzmannDistribution(cu, temperature=300*Kelvin)

# Print initial state
print(f'Initial T: {cu.get_temperature():.2f} K')
print(f'Initial E: {cu.get_total_energy():.2f} eV')

# Set up Langevin MD (5 fs timestep, 300K, 1e12 1/s friction)
md = Langevin(cu, timestep=5*fs, temperature=300*Kelvin, friction=1e12)

# Run 100 steps
md.run(100)

# Print final state
print(f'Final T: {cu.get_temperature():.2f} K')
print(f'Final E: {cu.get_total_energy():.2f} eV')
