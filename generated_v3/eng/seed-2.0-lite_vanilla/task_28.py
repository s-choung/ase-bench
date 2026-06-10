import ase.units as units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin

# Create 2x2x2 FCC Cu supercell
atoms = bulk('Cu', 'fcc', a=3.61).repeat((2, 2, 2))
atoms.calc = EMT()

# Simulation parameters
total_steps = 200
T_start = 300  # K
T_end = 600    # K
step_counter = 0

# Linear temperature ramp function
def update_temperature():
    global step_counter
    current_T = T_start + (T_end - T_start) * (step_counter / (total_steps - 1))
    dyn.set_temperature(current_T * units.kB)
    step_counter += 1

# Print temperature at intervals
def log_temperature():
    print(f"Step {step_counter:3d} | Current Temperature: {atoms.get_temperature():.1f} K")

# Initialize Langevin dynamics
dyn = Langevin(
    atoms,
    timestep=5 * units.fs,  # 5 fs timestep
    temperature=T_start * units.kB,
    friction=0.01 / units.ps,
    fixcm=True
)

# Attach functions to dynamics
dyn.attach(update_temperature, interval=1)
dyn.attach(log_temperature, interval=50)

# Run simulation
dyn.run(total_steps)
