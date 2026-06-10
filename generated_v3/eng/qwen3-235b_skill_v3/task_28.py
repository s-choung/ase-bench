from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

# Create Cu fcc 2x2x2 supercell
atoms = bulk('Cu', 'fcc') * (2, 2, 2)
atoms.calc = EMT()

# Initialize velocities at 300 K
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)  # Remove overall drift

# Setup Langevin thermostat
dyn = Langevin(atoms, timestep=5*units.fs, temperature_K=300, friction=0.01/units.fs)

# Temperature ramp parameters
initial_temp = 300
final_temp = 600
steps = 200
ramp_interval = steps // 4

def print_temp_and_ramp(atoms, dyn, step, ramp_step):
    current_temp = atoms.get_temperature()
    target_temp = initial_temp + (final_temp - initial_temp) * (step / steps)
    dyn.set_temperature(temperature_K=target_temp)
    if step % ramp_interval == 0:
        print(f"Step {step}: Current temp = {current_temp:.2f} K, Target = {target_temp:.2f} K")

# Run MD with temperature ramp
for step in range(steps):
    print_temp_and_ramp(atoms, dyn, step, ramp_interval)
    dyn.run(1)
