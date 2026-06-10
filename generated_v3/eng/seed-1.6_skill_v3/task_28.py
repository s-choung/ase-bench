from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

# Build Cu FCC 2x2x2 supercell
cu_super = bulk('Cu', 'fcc').repeat((2,2,2))
cu_super.calc = EMT()

# Initialize velocities
MaxwellBoltzmannDistribution(cu_super, temperature_K=300)
Stationary(cu_super)

# Langevin MD setup
timestep = 5 * units.fs
friction = 0.01 / units.fs
langevin = Langevin(cu_super, timestep=timestep, temperature_K=300, friction=friction)

# Temperature ramp parameters
start_temp, end_temp = 300.0, 600.0
total_steps = 200
temp_delta = (end_temp - start_temp) / total_steps

# Run ramp MD
for step in range(total_steps):
    langevin.temperature_K = start_temp + step * temp_delta
    langevin.step()
    if (step + 1) % 50 == 0:
        print(f'Step {step+1:3d}, Temp: {cu_super.get_temperature():.2f} K')
