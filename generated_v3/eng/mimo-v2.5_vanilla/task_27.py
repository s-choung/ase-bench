import numpy as np
from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.md import MolecularDynamics
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase import units

# Build Ag FCC 2x2x2 supercell
atoms = bulk('Ag', 'fcc', a=4.09, cubic=True)
atoms = atoms.repeat((2, 2, 2))
atoms.calc = EMT()

# Set initial temperature
MaxwellBoltzmannDistribution atoms, temperature_K=500)

# Run NVT MD with Bussi thermostat
md = MolecularDynamics(
    atoms,
    timestep=5.0 * units.fs,
    logfile='md.log',
    trajectory='md.traj'
)
md.attach(MolecularDynamics.attach_thermostat, md, temperature_K=500, tau=100.0 * units.fs)

# Alternatively, use the proper Bussi thermostat setup
from ase.md.bussi import BussiThermostat

# Create Bussi thermostat
thermostat = BussiThermostat(atoms, temperature_K=500, timestep=5.0 * units.fs)

# Run MD and record temperature every 50 steps
for i in range(200):
    thermostat.run(1)
    if (i + 1) % 50 == 0:
        temp = atoms.get_temperature()
        print(f"Step {i + 1}: Temperature = {temp:.2f} K")
