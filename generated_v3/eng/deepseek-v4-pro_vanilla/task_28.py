from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase import units

atoms = bulk('Cu', 'fcc', a=3.61).repeat((2, 2, 2))
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
dyn = Langevin(atoms, timestep=5 * units.fs, temperature_K=300, friction=0.01)

n_steps = 200
for step in range(1, n_steps + 1):
    T = 300 + (step / n_steps) * 300
    dyn.set_temperature(T)
    dyn.run(1)
    if step % 50 == 0:
        print(f"Step {step}, Temperature: {atoms.get_temperature():.2f} K")
