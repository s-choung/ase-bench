from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk('Cu', 'fcc', cubic=True) * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

dyn = Langevin(atoms, 5*units.fs, temperature_K=300, friction=0.01/units.fs)

print(f"Initial T = {atoms.get_temperature():.1f} K, E = {atoms.get_total_energy():.4f} eV")
dyn.run(100)
print(f"Final   T = {atoms.get_temperature():.1f} K, E = {atoms.get_total_energy():.4f} eV")
