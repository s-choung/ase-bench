from ase.build import bulk
from ase.md.langevin import Langevin
from ase.calculators.emt import EMT
from ase import units
import numpy as np

# FCC Cu 2x2x2 supercell
atoms = bulk('Cu', 'fcc').repeat((2,2,2))
atoms.calc = EMT()

nsteps = 200
dt = 5 * units.fs
t_start = 300
t_end = 600

def temperature_ramp(step):
    return t_start + (t_end - t_start) * step / nsteps

def step_hook(a=atoms, interval=50):
    step_hook.counter += 1
    if step_hook.counter % interval == 0:
        print(f"Step {step_hook.counter}: T = {a.get_temperature():.1f} K")
step_hook.counter = 0

for step in range(1, nsteps+1):
    temp = temperature_ramp(step)
    dyn = Langevin(atoms, dt, temp, friction=0.02)
    dyn.run(1)
    step_hook()
