from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase import units
atoms = bulk('Pd', 'fcc', a=3.92, cubic=True) * (2, 2, 2)
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=500)
dyn = VelocityVerlet(atoms, dt=2 * units.fs)
e0 = atoms.get_total_energy()
dyn.run(200)
print(atoms.get_total_energy() - e0)
