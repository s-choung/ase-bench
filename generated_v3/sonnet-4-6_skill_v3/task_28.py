import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True) * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

timestep = 5 * units.fs
total_steps = 200
T_start = 300.0
T_end = 600.0
interval = 50

step_counter = [0]

def run_ramp():
    for block in range(total_steps // interval):
        start_step = block * interval
        end_step = start_step + interval
        for s in range(interval):
            current_step = start_step + s
            T = T_start + (T_end - T_start) * current_step / (total_steps - 1)
            md = Langevin(atoms, timestep=timestep, temperature_K=T, friction=0.01 / units.fs)
            md.run(1)
        print(f"Step {end_step:4d} | Target T: {T_start + (T_end - T_start) * (end_step - 1) / (total_steps - 1):.1f} K | Actual T: {atoms.get_temperature():.1f} K")

run_ramp()
