from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary, ZeroRotation

atoms = bulk('Cu', 'fcc', a=3.6) * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, 300 * units.kB)
Stationary(atoms)
ZeroRotation(atoms)

dt = 5 * units.fs
friction = 0.01 / units.fs
n_steps = 200
md = Langevin(atoms, dt, 300, friction)

for step in range(n_steps):
    current_temp = 300 + 300 * step / (n_steps - 1)
    md.temperature_K = current_temp
    md.sigma = np.sqrt(2 * md.friction * md.temperature_K * md.dt / (units.kB * md.mass)) * np.sqrt(3)
    md.step()
    if step % 50 == 0 or step == n_steps - 1:
        print(f"Step {step}: set_temp = {current_temp:.2f} K, actual_temp = {atoms.get_temperature():.2f} K")
