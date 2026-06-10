from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase import units

atoms = bulk('Cu', 'fcc', cubic=True) * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)

print(f"Initial T: {atoms.get_temperature():.1f} K, E: {atoms.get_total_energy():.4f} eV")

dyn = Langevin(atoms, timestep=5 * units.fs, temperature_K=300, friction=0.02)
dyn.run(100)

print(f"Final   T: {atoms.get_temperature():.1f} K, E: {atoms.get_total_energy():.4f} eV")
