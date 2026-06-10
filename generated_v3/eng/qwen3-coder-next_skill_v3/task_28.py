from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

# Build Cu FCC 2x2x2 supercell
cu = bulk('Cu', 'fcc', a=3.61)
supercell = cu.repeat((2, 2, 2))

# Set up calculator
supercell.calc = EMT()

# Set initial temperature and velocity distribution
temperature = 300.0
MaxwellBoltzmannDistribution(supercell, temperature_K=temperature)
Stationary(supercell)

# Initialize Langevin dynamics
timestep = 5 * units.fs
friction = 0.01 / units.fs
md = Langevin(supercell, timestep=timestep, temperature_K=temperature, friction=friction)

# Run MD with temperature ramp and print temperature
steps = 200
temp_ramp = [300 + 150 * i / (steps // 50 - 1) for i in range(steps // 50)] if steps >= 50 else [300]

for i in range(steps):
    md.step()
    
    # Update temperature every 50 steps
    if (i + 1) % 50 == 0:
        step_num = (i + 1) // 50
        new_temp = temp_ramp[min(step_num - 1, len(temp_ramp) - 1)]
        md.set_temperature(temperature_K=new_temp)
        
        # Update velocity distribution to match new temperature
        MaxwellBoltzmannDistribution(supercell, temperature_K=new_temp)
        Stationary(supercell)
        
        # Print current temperature
        print(f"Step {i+1}: Temperature = {supercell.get_temperature():.1f} K")
