from ase.build import bulk
from ase.calculators.emt import EMT
from ase import units
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True) * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

print(f"Initial: T = {atoms.get_temperature():.1f} K, "
      f"Epot = {atoms.get_potential_energy():.4f} eV, "
      f"Etot = {atoms.get_potential_energy() + atoms.get_kinetic_energy():.4f} eV")

dyn = Langevin(atoms, timestep=5*units.fs, temperature_K=300, friction=0.01/units.fs)
dyn.run(100)

print(f"Final:   T = {atoms.get_temperature():.1f} K, "
      f"Epot = {atoms.get_potential_energy():.4f} eV, "
      f"Etot = {atoms.get_potential_energy() + atoms.get_kinetic_energy():.4f} eV")
