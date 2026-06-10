from ase import units
from ase.build import bulk
from ase.md.bussi import Bussi
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase.calculators.emt import EMT

# Create Ag FCC 2x2x2 supercell
atoms = bulk('Ag', 'fcc', cubic=True).repeat((2, 2, 2))
atoms.calc = EMT()

# Set initial velocities for 500K
MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)  # Remove center of mass drift

# Initialize Bussi thermostat
dyn = Bussi(atoms, timestep=5*units.fs, temperature_K=500)

# MD loop with temperature recording
for i in range(200):
    dyn.run(1)  # Run 1 step
    if (i+1) % 50 == 0:
        T = atoms.get_temperature()
        print(f'Step {i+1:4d}: Temperature = {T:.2f} K')
