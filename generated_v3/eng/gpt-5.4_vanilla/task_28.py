from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

atoms = bulk('Cu', 'fcc', a=3.61, cubic=True) * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

dyn = Langevin(atoms, timestep=5 * units.fs, temperature_K=300, friction=0.02)

nsteps = 200
t0, t1 = 300.0, 600.0

for step in range(1, nsteps + 1):
    T = t0 + (t1 - t0) * step / nsteps
    dyn.set_temperature(temperature_K=T)
    dyn.run(1)
    if step % 50 == 0:
        print(f"Step {step:3d}: T_target = {T:6.1f} K, T_inst = {atoms.get_temperature():6.1f} K")
