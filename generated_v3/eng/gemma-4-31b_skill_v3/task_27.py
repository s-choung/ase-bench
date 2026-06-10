from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.bussi import Bussi
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

# Setup system
atoms = bulk('Ag', 'fcc', a=4.08)
atoms = atoms * (2, 2, 2)
atoms.calc = EMT()

# Initialize velocities
MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

# MD Setup
timestep = 5 * units.fs
dyn = Bussi(atoms, timestep=timestep, temperature_K=500, time_constant=25 * units.fs)

# Run and monitor
for step in range(200):
    dyn.step()
    if (step + 1) % 50 == 0:
        print(f"Step {step+1}: Temp = {atoms.get_temperature():.2f} K")
