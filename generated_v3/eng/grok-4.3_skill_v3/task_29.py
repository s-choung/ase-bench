from ase import Atoms, units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk('Pd', 'fcc', a=3.95, cubic=True) * (2, 2, 2)
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)
dyn = VelocityVerlet(atoms, timestep=2 * units.fs)
e0 = atoms.get_total_energy()
dyn.run(200)
print(atoms.get_total_energy() - e0)
