from ase.build import bulk
from ase.md.langevin import Langevin
from ase.units import fs, kB
import numpy as np

atoms = bulk('Cu', 'fcc', a=3.6).repeat((2, 2, 2))
atoms.calc = atoms.get_calculator()  # use EMT

# Attach Maxwell-Boltzmann velocities at 300 K
atoms.set_momenta(np.random.normal(0, np.sqrt(kB * 300 / atoms.get_masses()[:, None]), (len(atoms), 3)))

dyn = Langevin(atoms, timestep=5 * fs, temperature=300 * kB, friction=0.002, rng=np.random.RandomState(42))

def print_temp():
    step = dyn.get_number_of_steps()
    temp = atoms.get_temperature()
    print(f"Step {step:3d}: T = {temp:.1f} K")

dyn.attach(print_temp, interval=50)

# Ramp temperature linearly from 300 K to 600 K over 200 steps
def ramp_temp():
    step = dyn.get_number_of_steps()
    T = 300 + 300 * step / 200
    dyn.set_temperature(T * kB)

dyn.attach(ramp_temp, interval=1)

dyn.run(200)
