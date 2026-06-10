from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary, ZeroRotation
from ase import units

atoms = bulk('Cu', 'fcc', a=3.615, cubic=True) * (2, 2, 2)
atoms.calc = EMT()

T0, T1 = 300.0, 600.0
nsteps = 200
dt = 5 * units.fs

MaxwellBoltzmannDistribution(atoms, temperature_K=T0)
Stationary(atoms)
ZeroRotation(atoms)

dyn = Langevin(atoms, dt, temperature_K=T0, friction=0.02)

def ramp_temperature():
    step = dyn.nsteps
    T = T0 + (T1 - T0) * step / nsteps
    dyn.set_temperature(temperature_K=T)
    if step % 50 == 0:
        print(f"Step {step:4d}: T = {T:.1f} K")

dyn.attach(ramp_temperature, interval=1)

dyn.run(nsteps)
