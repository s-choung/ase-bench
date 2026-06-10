from ase.build import bulk
from ase.md.langevin import Langevin
from ase import units
import numpy as np

atoms = bulk('Cu', 'fcc', a=3.6)
atoms = atoms * (2, 2, 2)
atoms.calc = 'EMT'

langevin = Langevin(atoms, timestep=5 * units.fs, temperature_K=300, friction=0.01 / units.fs)

temperature_target = 600
temperature_initial = 300
temperature_delta = (temperature_target - temperature_initial) / 200
current_temperature = temperature_initial

for i in range(200):
    langevin.run(1)
    current_temperature = atoms.get_temperature()
    if i % 50 == 0:
        print(f"Step {i+1}: Temperature = {current_temperature:.2f} K")
