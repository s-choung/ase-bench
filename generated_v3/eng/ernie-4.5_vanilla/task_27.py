from ase.build import bulk
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.verlet import VelocityVerlet
from ase.calculators.emt import EMT
from ase.md import MDLogger
from ase.md.bussi import BussiThermostat

# Create FCC Ag supercell
atoms = bulk('Ag', 'fcc', a=4.09, cubic=True).repeat((2, 2, 2))

# Set calculator
atoms.calc = EMT()

# Set momentum to zero
atoms.set_momentum(0)

# Assign initial velocities according to Maxwell-Boltzmann distribution at 500K
MaxwellBoltzmannDistribution(atoms, 500 * 3.167e-6)  # Units: temp in K, time in fs

# Create MD object with a timestep of 5 fs
dyn = VelocityVerlet(atoms, 5 * 1e-3,  # 5 fs in ps units
                     trajectory=None,  # No trajectory file
                     logfile=None)     # No logfile

# Attach Bussi thermostat for NVT ensemble at 500K
dyn.attach(BussiThermostat(atoms, 500 * 3.167e-6, interval=1), interval=1)  # Interval in steps

# Create logger to record temperature every 50 steps
logger = MDLogger(dyn, atoms, '-', header=False, stress=False, peratom=False, mode="a")
dyn.attach(logger, interval=50)

# Run MD for 200 steps
dyn.run(200)

# Print the final temperature (optional, as logger already records it)
print(f"Final Temperature: {atoms.get_temperature() / 3.167e-6:.2f} K")
