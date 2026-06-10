import numpy as np
from ase import units
from ase.build import bulk
from ase.md.bussi import Bussi
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase.calculators.emt import EMT

# Setup Ag FCC supercell
atoms = bulk('Ag', 'fcc', a=4.09)
atoms = atoms.repeat((2, 2, 2))
atoms.calc = EMT()

# Initial velocity and COM removal
MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

# MD setup: Bussi thermostat (NVT)
timestep = 5 * units.fs
dyn = Bussi(atoms, timestep=timestep, temperature_K=500, reuse_forces=True)

# Logging function
def print_temp(step):
    if step % 50 == 0:
        print(f"Step: {step}, Temp: {atoms.get_temperature():.2f} K")

dyn.attach(print_temp, interval=1)

# Run simulation
dyn.run(200)
