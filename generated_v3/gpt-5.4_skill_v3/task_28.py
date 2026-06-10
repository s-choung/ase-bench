from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True) * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

dt = 5 * units.fs
nsteps = 200
t0, t1 = 300.0, 600.0
friction = 0.01 / units.fs

dyn = Langevin(atoms, timestep=dt, temperature_K=t0, friction=friction)

for step in range(1, nsteps + 1):
    target_T = t0 + (t1 - t0) * step / nsteps
    dyn.set_temperature(temperature_K=target_T)
    dyn.run(1)
    if step % 50 == 0:
        print(f"step {step:3d} target_T={target_T:7.2f}K current_T={atoms.get_temperature():7.2f}K")
