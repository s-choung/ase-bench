from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk('Cu', 'fcc') * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

total_steps = 200
dt = 5 * units.fs
T0, T1 = 300, 600

for i in range(0, total_steps, 50):
    T_target = T0 + (T1 - T0) * (i + 50) / total_steps
    Langevin(atoms, dt, temperature_K=T_target, friction=0.002/units.fs).run(50)
    print(f"Step {i + 50}: T = {atoms.get_temperature():.1f} K")
