from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase import units
from ase.io import Trajectory
import numpy as np

atoms = bulk('Cu', 'fcc', a=3.615).repeat((2, 2, 2))
atoms.calc = EMT()

T0, T1 = 300.0, 600.0
nsteps = 200
dt = 5 * units.fs

MaxwellBoltzmannDistribution(atoms, temperature_K=T0)

dyn = Langevin(atoms, dt, temperature_K=T0, friction=0.02)

def target_temperature(step):
    return T0 + (T1 - T0) * step / (nsteps - 1)

def update_temperature():
    step = dyn.nsteps
    T = target_temperature(step)
    dyn.set_temperature(temperature_K=T)

def print_temp():
    T = atoms.get_temperature()
    print(f"Step {dyn.nsteps:4d}: T = {T:.2f} K")

dyn.attach(update_temperature, interval=1)
dyn.attach(print_temp, interval=50)

dyn.run(nsteps)
