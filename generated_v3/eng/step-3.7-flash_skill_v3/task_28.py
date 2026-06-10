from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk('Cu', 'fcc', a=3.6) * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

dyn = Langevin(atoms, 5*units.fs, temperature_K=300, friction=0.01/units.fs)

for step in range(200):
    dyn.temperature = (300 + (600 - 300) * (step + 1) / 200) * units.kB
    dyn.run(1)
    if (step + 1) % 50 == 0:
        print(f"Step {step+1}: {atoms.get_temperature():.1f} K")
