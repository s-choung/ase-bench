from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary, ZeroRotation
from ase import units

atoms = bulk('Cu', 'fcc', a=3.615).repeat((2, 2, 2))
atoms.calc = EMT()

T0 = 300.0
T1 = 600.0
nsteps = 200
dt = 5.0 * units.fs
friction = 0.02

MaxwellBoltzmannDistribution(atoms, temperature_K=T0)
Stationary(atoms)
ZeroRotation(atoms)

dyn = Langevin(atoms, dt, temperature_K=T0, friction=friction)

def current_temperature(a):
    return 2.0 * a.get_kinetic_energy() / (3.0 * len(a) * units.kB)

for step in range(1, nsteps + 1):
    T = T0 + (T1 - T0) * step / nsteps
    dyn.set_temperature(temperature_K=T)
    dyn.run(1)
    if step % 50 == 0:
        print(f"Step {step:3d}: target T = {T:6.1f} K, current T = {current_temperature(atoms):6.1f} K")
