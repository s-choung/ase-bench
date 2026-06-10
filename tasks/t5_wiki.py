"""T5 Wiki: Langevin MD of Cu at 300K"""
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True) * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

dyn = Langevin(atoms, timestep=5.0 * units.fs, temperature_K=300,
               friction=0.01 / units.fs)
dyn.run(20)
print(f"Final energy: {atoms.get_potential_energy():.4f} eV")
print(f"Temperature: {atoms.get_temperature():.1f} K")
print(f"Kinetic energy: {atoms.get_kinetic_energy():.4f} eV")
