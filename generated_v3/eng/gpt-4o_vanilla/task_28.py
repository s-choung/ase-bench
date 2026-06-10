from ase.build import bulk
from ase.md.langevin import Langevin
from ase.calculators.emt import EMT
from ase import units
import numpy as np

cu = bulk('Cu', 'fcc', a=3.6) * (2, 2, 2)
cu.calc = EMT()
start_temp, end_temp = 300, 600

def ramp_temperature(step, total_steps):
    return start_temp + (end_temp - start_temp) * step / total_steps

def print_temperature(atoms, step):
    if step % 50 == 0:
        temp = atoms.get_kinetic_energy() / (1.5 * units.kB * len(atoms))
        print(f"Step {step}: T = {temp:.2f} K")

dyn = Langevin(cu, timestep=5 * units.fs, temperature_lambda=ramp_temperature, friction=0.02)

for step in range(200):
    dyn.set_temperature(ramp_temperature(step, 200))
    dyn.run(1)
    print_temperature(cu, step)
