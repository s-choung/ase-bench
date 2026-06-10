from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.verlet import VelocityVerlet
from ase.md.thermostats import Bussi
from ase import units

# Create 2x2x2 FCC Ag supercell
atoms = bulk('Ag', 'fcc', a=4.09).repeat((2, 2, 2))
atoms.set_calculator(EMT())

# Initial velocities at 300 K
temp_target = 300.0  # K
MaxwellBoltzmannDistribution(atoms, temp_target)

# MD parameters
dt = 5 * units.fs          # 5 fs
steps = 200
interval = 50

# Bussi thermostat (tau ~ 100 fs)
thermostat = Bussi(atoms, dt, temperature=temp_target, taut=100 * units.fs)

# Velocity Verlet integrator with thermostat
dyn = VelocityVerlet(atoms, dt, thermostat=thermostat)

# Print temperature every `interval` steps
def print_temp(atoms, step):
    print(f"Step {step:4d}: Temp = {atoms.get_temperature():.2f} K")
dyn.attach(print_temp, interval=interval)

# Run dynamics
dyn.run(steps)
