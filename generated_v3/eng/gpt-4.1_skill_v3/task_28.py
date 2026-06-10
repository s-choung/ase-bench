from ase.build import bulk
from ase.calculators.emt import EMT
from ase import units
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
import numpy as np

atoms = bulk('Cu', 'fcc') * (2,2,2)
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

steps = 200
dt = 5 * units.fs
T0, T1 = 300, 600

dyn = Langevin(atoms, timestep=dt, temperature_K=T0, friction=0.01/units.fs)

for step in range(steps):
    curr_T = T0 + (T1 - T0) * step / (steps - 1)
    dyn.temperature_K = curr_T
    dyn.run(1)
    if (step + 1) % 50 == 0 or step == 0:
        print(f"Step {step+1:3d}, T = {atoms.get_temperature():.1f} K")
