from ase import Atoms
from ase.calculators.emt import EMT
from ase.md.bussi import Bussi
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
import numpy as np
from ase import units

# Create an Ag FCC 2x2x2 supercell
atoms = bulk('Ag', 'fcc', a=4.09)
atoms = atoms.repeat((2, 2, 2))

# Set the calculator
atoms.calc = EMT()

# Set up the Bussi thermostat
bussi = Bussi(atoms, timestep=5 * units.fs, temperature_K=500, barostat=True)

# Initialize velocities
MaxwellBoltzmannDistribution(atoms, temperature_K=500)

# Remove COM drift
Stationary(atoms)

# Run the MD simulation
for i in range(200):
    bussi.run(1)
    if i % 50 == 0:
        temp = atoms.get_temperature()
        print(f"Step {i}: Temperature = {temp:.2f} K")
