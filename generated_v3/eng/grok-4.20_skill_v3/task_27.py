from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.bussi import Bussi
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk('Ag', 'fcc', cubic=True) * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

md = Bussi(atoms, timestep=5*units.fs, temperature_K=500, friction=0.01/units.fs)

for step in range(200):
    md.run(1)
    if step % 50 == 0:
        print(f"Step {step}: T = {atoms.get_temperature():.1f} K")
