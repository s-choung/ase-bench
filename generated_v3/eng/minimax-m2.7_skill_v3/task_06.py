from ase import units
from ase.build import bulk
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk('Cu', 'fcc', a=3.6)
atoms *= (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

print(f"Initial T = {atoms.get_temperature():.1f} K")
print(f"Initial E = {atoms.get_potential_energy():.4f} eV")

Langevin(atoms, timestep=5*units.fs, temperature_K=300, friction=0.01/units.fs).run(100)

print(f"Final T = {atoms.get_temperature():.1f} K")
print(f"Final E = {atoms.get_potential_energy():.4f} eV")
