from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

atoms = bulk('Cu', 'fcc', a=3.6) * (2, 2, 2)
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)
print(f"Initial Temp: {atoms.get_temperature():.2f} K")
print(f"Initial Energy: {atoms.get_potential_energy():.4f} eV")
 Langevin(atoms, 5 * units.fs, 300, 0.01 / units.fs).run(100)
print(f"Final Temp: {atoms.get_temperature():.2f} K")
print(f"Final Energy: {atoms.get_potential_energy():.4f} eV")
