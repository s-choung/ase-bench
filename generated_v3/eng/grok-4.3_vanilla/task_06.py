from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase import units
atoms = bulk('Cu', 'fcc', cubic=True) * (2, 2, 2)
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
dyn = Langevin(atoms, 5 * units.fs, temperature_K=300, friction=0.01)
print(atoms.get_temperature(), atoms.get_potential_energy())
dyn.run(100)
print(atoms.get_temperature(), atoms.get_potential_energy())
