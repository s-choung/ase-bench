from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase import units

# Create 2x2x2 FCC Cu supercell
atoms = bulk('Cu', 'fcc', a=3.615)
atoms = atoms.repeat(2)

# Set calculator
atoms.calc = EMT()

# Initialize Langevin dynamics
timestep = 5 * units.fs
temperature = 300  # Starting temperature
friction = 0.002

dyn = Langevin(
    atoms,
    timestep=timestep,
    temperature_K=temperature,
    friction=friction,
    logfile='-'
)

# Temperature ramp: 300K → 600K over 200 steps
def print_temperature():
    step = dyn.nsteps
    if step % 50 == 0:
        current_temp = dyn.temperature_K()
        print(f"Step {step}: T = {current_temp:.1f} K")

dyn.attach(print_temperature, interval=50)

# Run dynamics with temperature ramp
for step in range(200):
    # Linear temperature increase
    target_temp = 300 + (600 - 300) * step / 199
    dyn.set_temperature(target_temp)
    dyn.step()
