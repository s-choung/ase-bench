from ase import Atoms
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.units import fs, kB
import numpy as np

a = 3.6
cu = Atoms('Cu', cell=(a, a, a), pbc=True)
cu *= (2, 2, 2)
cu.calc = EMT()

def print_temp():
    if md.get_number_of_steps() % 50 == 0:
        print(f"Step: {md.get_number_of_steps()}, Temp: {md.get_temperature():.1f} K")

def temp_ramp():
    steps = md.get_number_of_steps()
    return 300 + 300 * steps / 200

md = Langevin(cu, 5 * fs, temperature_K=temp_ramp, friction=0.02)
md.attach(print_temp, interval=1)
md.run(200)
