from ase.build import bulk
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.units import fs, kB
import numpy as np

atoms = bulk('Ag', 'fcc', a=4.09).repeat((2, 2, 2))
atoms.calc = atoms.get_calculator()  # EMT by default for Ag

MaxwellBoltzmannDistribution(atoms, temperature_K=500.0)

dt = 5.0 * fs
dyn = Langevin(atoms, timestep=dt, temperature_K=500.0, friction=0.002, rng=np.random.RandomState(42))

def print_temp():
    print(f"Step: {dyn.get_number_of_steps():4d}  T: {atoms.get_temperature():6.1f} K")

dyn.attach(print_temp, interval=50)
dyn.run(200)
