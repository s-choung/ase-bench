from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms = atoms.repeat((2, 2, 2))
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

print(f'Initial temperature: {atoms.get_temperature():.2f} K')
print(f'Initial energy: {atoms.get_potential_energy():.3f} eV')

md = Langevin(atoms, timestep=5*units.fs, temperature_K=300, friction=0.01/units.fs)
md.run(100)

print(f'Final temperature: {atoms.get_temperature():.2f} K')
print(f'Final energy: {atoms.get_potential_energy():.3f} eV')
