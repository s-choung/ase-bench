from ase import Atoms
from ase.lattice.cubic import FaceCenteredCubic
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.units import fs, kB
import numpy as np

# Create Ag FCC 2x2x2 supercell
ag = FaceCenteredCubic('Ag', size=(2, 2, 2), pbc=True)

# Set up EMT calculator
from ase.calculators.emt import EMT
ag.calc = EMT()

# Set initial temperature and velocities
temperature = 500  # K
MaxwellBoltzmannDistribution(ag, temperature)

# Set up Langevin thermostat (Bussi-like with noise)
# Langevin is the ASE implementation of the Bussi-Donadio-Parrinello thermostat
dt = 5 * fs  # timestep
damping = 1.0 / (100 * fs)  # 100 fs relaxation time
 langevin = Langevin(ag, dt, temperature_K=temperature, friction=damping)

# Run MD and record temperature every 50 steps
print("Step\tTemperature (K)")
for step in range(500):
    langevin.run(1)
    kinetic_energy = 0.5 * np.sum(ag.get_masses()[:, np.newaxis] * ag.get_velocities()**2)
    temperature_now = (2 * kinetic_energy / (3 * len(ag) * kB))
    if (step + 1) % 50 == 0:
        print(f"{step + 1}\t{temperature_now:.1f}")
