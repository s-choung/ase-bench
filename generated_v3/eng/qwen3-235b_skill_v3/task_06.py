from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution

atoms = bulk('Cu', 'fcc') * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
print(f"Initial temperature: {atoms.get_temperature():.2f} K")
print(f"Initial energy: {atoms.get_potential_energy():.3f} eV")

trajectory = []
dyn = Langevin(atoms, timestep=5 * units.fs, temperature_K=300, friction=0.01 / units.fs)
dyn.attach(lambda: trajectory.append(atoms.copy()), interval=1)
dyn.run(100)

print(f"Final temperature: {atoms.get_temperature():.2f} K")
print(f"Final energy: {atoms.get_potential_energy():.3f} eV")
