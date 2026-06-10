from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

# Create Cu FCC 2x2x2 supercell
atoms = bulk('Cu', 'fcc', a=3.6) * (2, 2, 2)
atoms.calc = EMT()

# Initialise velocities at 300 K
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

# Set up Langevin dynamics
timestep = 5 * units.fs
dyn = Langevin(atoms, timestep=timestep, temperature_K=300,
               friction=0.01 / units.fs)

# Temperature ramp: 300 K → 600 K over 200 steps
nsteps = 200
T_start = 300
T_end = 600

for i in range(nsteps):
    # Linearly update thermostat temperature
    T = T_start + (T_end - T_start) * i / (nsteps - 1)
    dyn.set_temperature(temperature_K=T)
    dyn.run(1)

    if (i + 1) % 50 == 0:
        current_T = atoms.get_temperature()
        print(f"Step {i+1}: T = {current_T:.1f} K")
