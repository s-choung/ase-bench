from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

atoms = bulk('Cu', 'fcc', cubic=True) * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

total_steps = 200
chunk = 50
T_start, T_end = 300, 600

dyn = Langevin(atoms, timestep=5 * units.fs, temperature_K=T_start, friction=0.01 / units.fs)

for i in range(total_steps // chunk):
    T = T_start + (T_end - T_start) * (i * chunk) / total_steps
    dyn.set_temperature(temperature_K=T)
    dyn.run(chunk)
    print(f"Step {(i+1)*chunk:4d} | T_current = {atoms.get_temperature():7.1f} K | T_target = {T:5.1f} K")
