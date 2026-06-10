from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True) * (2, 2, 2)
atoms.calc = EMT()

dt = 5 * units.fs
nsteps = 200
t0, t1 = 300.0, 600.0

MaxwellBoltzmannDistribution(atoms, temperature_K=t0)
Stationary(atoms)

dyn = Langevin(atoms, timestep=dt, temperature_K=t0, friction=0.01 / units.fs)

def ramp_temperature():
    step = dyn.nsteps
    T = t0 + (t1 - t0) * step / nsteps
    dyn.set_temperature(temperature_K=T)

def report():
    print(f"step {dyn.nsteps:4d}  T = {atoms.get_temperature():.2f} K")

dyn.attach(ramp_temperature, interval=1)
dyn.attach(report, interval=50)

dyn.run(nsteps)
