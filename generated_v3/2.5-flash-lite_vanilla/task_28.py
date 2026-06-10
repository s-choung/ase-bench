from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.optimize import BFGS
from ase import units
import numpy as np

# Cu FCC 2x2x2 supercell 생성
atoms = fcc111('Cu', size=(2, 2, 2), vacuum=10.0)
atoms.calc = EMT()

# 초기 온도 설정 (300K)
initial_temp = 300.0
final_temp = 600.0
n_steps = 200
dt = 5.0 * units.fs
temperature_profile = np.linspace(initial_temp, final_temp, n_steps)

# Langevin dynamics 설정
thermostat = Langevin(atoms, timestep=dt, temperature=temperature_profile[0], friction=0.01)

# MD 시뮬레이션
for i in range(n_steps):
    thermostat.set_temperature(temperature_profile[i])
    thermostat.run(1)
    if (i + 1) % 50 == 0:
        print(f"Step {i+1}: Temperature = {atoms.get_temperature():.2f} K")
