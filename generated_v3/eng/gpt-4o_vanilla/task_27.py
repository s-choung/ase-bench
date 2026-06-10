from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.bussi import Bussi
from ase.md import MDLogger
from ase.io.trajectory import Trajectory
import numpy as np

# Create Ag FCC 2x2x2 supercell
atoms = bulk('Ag', 'fcc', a=4.09) * (2, 2, 2)
atoms.calc = EMT()

# Initialize velocities
MaxwellBoltzmannDistribution(atoms, temperature_K=500)

# Set up Bussi thermostat
timestep = 5 * 1e-15  # 5 fs
thermostat = Bussi(atoms, timestep, temperature_K=500)

# Logger
log = MDLogger(thermostat, atoms, 'md.log', header=True, stress=False, peratom=False)
thermostat.attach(log, interval=50)

# Run MD
thermostat.run(200 * timestep)

# Output temperature every 50 steps
with open('md.log') as f:
    for line in f:
        if 'T=' in line:
            print('Temperature:', float(line.split()[8]), 'K')
