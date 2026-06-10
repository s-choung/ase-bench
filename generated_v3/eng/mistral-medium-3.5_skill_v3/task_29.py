from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

atoms = bulk('Pd', 'fcc', a=3.9)
atoms = atoms * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)
dyn = VelocityVerlet(atoms, timestep=2 * units.fs)

E0 = atoms.get_total_energy()
dyn.run(200)
E1 = atoms.get_total_energy()
print(E1 - E0)
