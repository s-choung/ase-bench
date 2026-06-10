from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.bussi import Bussi
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution

# Create Ag FCC 2x2x2 supercell
atoms = bulk('Ag', 'fcc', a=4.09).repeat((2, 2, 2))
atoms.calc = EMT()

# Initialize velocities to 500K
MaxwellBoltzmannDistribution(atoms, temperature_K=500)

# Set up Bussi NVT MD
def print_temperature():
    print(f"Step {md.nsteps:3d} | Temperature: {atoms.get_temperature():.1f} K")

md = Bussi(atoms, timestep=5, temperature_K=500, tt=0.1)
md.attach(print_temperature, interval=50)

# Run 200 steps of MD
md.run(200)
