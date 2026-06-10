from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units
import numpy as np

atoms = bulk('Cu', 'fcc', a=3.615) * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

dyn = Langevin(atoms, timestep=5*units.fs, temperature_K=300, friction=0.01/units.fs)

def temperature_ramp(step):
    return 300 + (600 - 300) * min(step, 200) / 200

def print_temperature(a=atoms):
    step = dyn.get_number_of_steps()
    if step % 50 == 0:
        temp = temperature_ramp(step)
        dyn.set_temperature(temp)
        print(f"Step {step:3d}: Target T = {temp:.1f} K, Actual T = {a.get_temperature():.1f} K")

dyn.attach(print_temperature, interval=1)
dyn.run(200)
