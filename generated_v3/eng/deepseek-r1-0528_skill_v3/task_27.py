from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.bussi import Bussi
from ase import units
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

# Create Ag FCC 2x2x2 supercell
atoms = bulk('Ag', 'fcc', a=4.09).repeat((2, 2, 2))

# Set calculator
atoms.calc = EMT()

# Initialize velocities at 500K
MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)  # Remove COM velocity

# Set up Bussi (NVT) thermostat
dyn = Bussi(atoms, timestep=5*units.fs, temperature=500*units.kB, friction=0.01)

# Run MD for 200 steps, print temperature every 50 steps
for i in range(4):
    dyn.run(50)  # Run 50 steps at a time
    print(f'Step {(i+1)*50}: T = {atoms.get_temperature():.2f} K')
