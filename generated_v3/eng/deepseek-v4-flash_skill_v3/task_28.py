from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

# Build Cu FCC 2x2x2 supercell
atoms = bulk('Cu', 'fcc', a=3.615) * (2, 2, 2)
atoms.calc = EMT()

# Initialize velocities
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

# Langevin MD
dyn = Langevin(atoms, timestep=5 * units.fs, temperature_K=300, friction=0.01 / units.fs)

nsteps = 200
T0, T1 = 300.0, 600.0

for step in range(nsteps):
    T = T0 + (T1 - T0) * step / (nsteps - 1)  # linear ramp
    dyn.temperature = T
    dyn.step()
    if (step + 1) % 50 == 0:
        print(f"Step {step+1}, Temperature: {atoms.get_temperature():.2f} K")
