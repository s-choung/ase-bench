from ase.build import bulk
from ase import units
from ase.calculators.emt import EMT
from ase.md.bussi import Bussi
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

# Build Ag FCC 2x2x2 supercell
atoms = bulk('Ag', 'fcc', a=4.09)
atoms *= (2, 2, 2)

# Assign built-in EMT calculator
atoms.calc = EMT()

# Initialize thermal velocities and remove center-of-mass drift
MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

# Logging function to print temperature at intervals
def log_status():
    step = dyn.get_number_of_steps()
    current_temp = atoms.get_temperature()
    print(f"Step {step:3d} | Temperature: {current_temp:.2f} K")

# Set up Bussi NVT thermostat
dyn = Bussi(
    atoms,
    timestep=5 * units.fs,
    temperature_K=500,
    taut=100 * units.fs  # Standard thermostat relaxation time
)

# Attach logger to run every 50 steps
dyn.attach(log_status, interval=50)

# Run 200 total MD steps
dyn.run(200)
