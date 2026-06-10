from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase import units

atoms = bulk('Cu', 'fcc', cubic=True) * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300.0)
dyn = Langevin(atoms, 5 * units.fs, temperature_K=300.0, friction=0.01)

print(f"Step   0 | T = {atoms.get_temperature():.1f} K")
for i in range(1, 5):
    dyn.set_temperature(temperature_K=300.0 + i * 75.0)
    dyn.run(50)
    print(f"Step {i*50:3d} | T = {atoms.get_temperature():.1f} K")
