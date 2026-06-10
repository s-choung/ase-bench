from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.bussi import Bussi
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units
import numpy as np

# Build Ag FCC 2x2x2 supercell
atoms = bulk('Ag', 'fcc', a=4.09)
atoms = atoms * (2, 2, 2)
atoms.calc = EMT()

# Set initial temperature and remove drift
MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

# Setup Bussi thermostat
timestep = 5 * units.fs
bussi = Bussi(atoms, timestep=timestep, temperature_K=500, tau=100*timestep)

# Run MD and record temperature every 50 steps
for step in range(200):
    bussi.run(1)
    if (step + 1) % 50 == 0:
        temp = atoms.get_temperature()
        print(f'Step {step+1:3d}: Temperature = {temp:.2f} K')
