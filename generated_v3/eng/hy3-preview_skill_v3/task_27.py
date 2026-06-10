from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.bussi import Bussi
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units
import numpy as np

# Create Ag FCC supercell
ag = bulk('Ag', 'fcc', a=4.09, cubic=True)
ag_supercell = ag.repeat((2, 2, 2))

# Set calculator
ag_supercell.calc = EMT()

# Initialize velocities for 500K
MaxwellBoltzmannDistribution(ag_supercell, temperature_K=500)
Stationary(ag_supercell)

# Set up NVT MD with Bussi thermostat
dyn = Bussi(ag_supercell, 
            timestep=5*units.fs,
            temperature_K=500)

# MD run with temperature recording
print("Step\tTemperature (K)")
for step in range(0, 201, 50):
    if step > 0:
        dyn.run(50)
    temp = ag_supercell.get_temperature()
    print(f"{step}\t{temp:.2f}")
