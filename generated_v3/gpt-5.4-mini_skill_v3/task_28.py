from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

atoms = bulk('Cu', 'fcc', a=3.6) * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

dt = 5 * units.fs
nsteps = 200
t0, t1 = 300.0, 600.0

dyn = Langevin(atoms, timestep=dt, temperature_K=t0, friction=0.01 / units.fs)

def update_temperature():
    step = dyn.nsteps
    T = t0 + (t1 - t0) * step / (nsteps - 1)
    dyn.set_temperature(T)

def log_temperature():
    print(f"step {dyn.nsteps:4d}  T = {atoms.get_temperature():.2f} K")

dyn.attach(update_temperature, interval=1)
dyn.attach(log_temperature, interval=50)

dyn.run(nsteps)
