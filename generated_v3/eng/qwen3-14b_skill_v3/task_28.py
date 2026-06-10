from ase import Atoms, units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase.md.langevin import Langevin

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True) * (2, 2, 2)
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

for step in range(200):
    temp = 300 + 1.5 * step
    dyn = Langevin(atoms, timestep=5*units.fs, temperature_K=temp, friction=0.01/units.fs)
    dyn.run(steps=1)
    if step % 50 == 0:
        print(f"Step {step}, Temperature: {atoms.get_temperature():.2f} K")
