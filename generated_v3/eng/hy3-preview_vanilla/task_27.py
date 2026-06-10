from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.bussi import Bussi
from ase import units
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution

# Create Ag FCC 2x2x2 supercell
atoms = bulk('Ag', 'fcc', a=4.09, cubic=True).repeat((2,2,2))
atoms.calc = EMT()

# Initialize velocities for 500K
MaxwellBoltzmannDistribution(atoms, temperature_K=500)

# Set up Bussi thermostat NVT at 500K
thermostat = Bussi(atoms, timestep=5*units.fs, temperature_K=500)

# MD run for 200 steps
steps = 200
for step in range(steps):
    thermostat.run(1)
    if step % 50 == 0 or step == steps-1:
        temp = atoms.get_temperature()
        print(f"Step {step}: Temperature = {temp:.2f} K")
