from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units
import numpy as np

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True) * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

dyn = Langevin(atoms, timestep=5 * units.fs, temperature_K=300,
               friction=0.01 / units.fs)

nsteps = 200
temps = np.linspace(300, 600, nsteps)

for i in range(nsteps):
    dyn.set_temperature(temperature_K=temps[i])
    dyn.run(1)
    if (i + 1) % 50 == 0:
        print(f"Step {i+1}: target T = {temps[i]:.1f} K, "
              f"current T = {atoms.get_temperature():.1f} K")
