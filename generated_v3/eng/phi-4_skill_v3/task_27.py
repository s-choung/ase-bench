from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md import Bussi
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.verlet import VelocityVerlet
from ase import units

# Create a 2x2x2 FCC supercell of Ag
atoms = bulk('Ag', 'fcc', a=4.08)  # a=4.08 angstroms for Ag
atoms *= (2, 2, 2)

# Set calculator
atoms.calc = EMT()

# Assign initial velocities corresponding to 500K
MaxwellBoltzmannDistribution(atoms, temperature_K=500)

# Set up MD simulation
timestep = 5 * units.fs
n_steps = 200
thermostat = Bussi(atoms, timestep=timestep, temperature_K=500)
md = VelocityVerlet(thermostat, timestep)
md.attach(lambda step: print(f"Step: {step}, Temp: {atoms.get_temperature()} K"), interval=50)

# Run the MD simulation
md.run(n_steps)
