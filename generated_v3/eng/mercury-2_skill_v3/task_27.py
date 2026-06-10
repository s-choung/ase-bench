from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.bussi import Bussi
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

# Build Ag FCC 2x2x2 supercell
atoms = bulk('Ag', 'fcc', a=4.09) * (2, 2, 2)
atoms.calc = EMT()

# Initialise velocities at 500 K and remove centre‑of‑mass motion
MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

# Bussi NVT thermostat (timestep = 5 fs)
dyn = Bussi(atoms,
            timestep=5 * units.fs,
            temperature_K=500,
            friction=0.01 / units.fs)   # default friction value

# Callback to print temperature every 50 steps
def print_temp(md):
    step = md.get_number_of_steps()
    temp = md.atoms.get_temperature()
    print(f"Step {step:3d} – Temperature: {temp:6.2f} K")

dyn.attach(print_temp, interval=50)

# Run 200 MD steps
dyn.run(200)
