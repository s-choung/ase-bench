from ase.build import bulk
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.nvtberendsen import NVTBerendsen
from ase.calculators.emt import EMT
import numpy as np

# Create Ag FCC 2x2x2 supercell
atoms = bulk('Ag', 'fcc', a=4.09, cubic=True).repeat((2, 2, 2))
atoms.calc = EMT()

# Set initial momenta
MaxwellBoltzmannDistribution(atoms, temperature_K=500)

# NVT ensemble with Bussi thermostat
dyn = NVTBerendsen(atoms, timestep=5 * femtosecond, temperature_K=500, taut=0.1 * picosecond)

# Function to print temperature
def print_temperature(atoms, step):
    if step % 50 == 0:
        print(f'Step {step}: Temperature = {atoms.get_temperature()} K')

# Run MD for 200 steps
dyn.attach(print_temperature, interval=1)
dyn.run(200)
