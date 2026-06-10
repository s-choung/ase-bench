from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase import units

atoms = bulk('Cu', crystalstructure='fcc') * (2, 2, 2)
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=300)

print(f"Initial T: {atoms.get_temperature():.2f} K, E: {atoms.get_potential_energy():.4f} eV")

dyn = Langevin(atoms, 5 * units.fs, temperature_K=300, friction=0.05)
dyn.run(100)

print(f"Final T: {atoms.get_temperature():.2f} K, E: {atoms.get_potential_energy():.4f} eV")
