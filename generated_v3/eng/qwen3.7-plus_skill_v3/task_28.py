from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

# 1. Build Cu FCC 2x2x2 supercell
atoms = bulk('Cu', 'fcc', a=3.6) * (2, 2, 2)
atoms.calc = EMT()

# 2. Initialize velocities and remove COM drift
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

# 3. Define temperature ramp callable (t is time in femtoseconds)
total_time_fs = 200 * 5.0

def temp_ramp(t):
    return 300.0 + 300.0 * (t / total_time_fs)

# 4. Setup Langevin dynamics
dyn = Langevin(
    atoms, 
    timestep=5 * units.fs, 
    temperature_K=temp_ramp, 
    friction=0.01 / units.fs
)

# 5. Attach observer to print temperature every 50 steps
def log_temperature():
    print(f"Step {dyn.get_number_of_steps()}, Temperature: {atoms.get_temperature():.1f} K")

dyn.attach(log_temperature, interval=50)

# 6. Run MD
dyn.run(200)
