from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.bussi import Bussi
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

# Build Ag FCC 2x2x2 supercell
ag_supercell = bulk('Ag', 'fcc').repeat((2, 2, 2))
ag_supercell.calc = EMT()

# Initialize velocities and remove COM drift
MaxwellBoltzmannDistribution(ag_supercell, temperature_K=500)
Stationary(ag_supercell)

# Callback to print temperature every 50 steps
def print_temperature(atoms, step):
    temp = atoms.get_temperature()
    print(f'Step {step:3d}, Temperature: {temp:.2f} K')

# Set up Bussi NVT thermostat (5 fs timestep)
md = Bussi(ag_supercell, timestep=5 * units.fs, temperature_K=500)
md.attach(print_temperature, interval=50)

# Run 200 MD steps
md.run(steps=200)
