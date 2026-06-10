from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk('Cu', 'fcc', a=3.6) * (2, 2, 2)
atoms.calc = EMT()

# Initialize velocities at starting temperature
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

# Set up Langevin dynamics
dyn = Langevin(atoms, timestep=5*units.fs, temperature_K=300, friction=0.01/units.fs)

def print_temp():
    print(f"Temperature: {atoms.get_temperature():.2f} K")

# Attach temperature print every 50 steps
dyn.attach(print_temp, interval=50)

# Run temperature ramp
for step in range(200):
    # Linearly increase temperature during the run
    current_temp = 300 + (600 - 300) * step / 199
    dyn.set_temperature(temperature_K=current_temp)
    dyn.run(1)
