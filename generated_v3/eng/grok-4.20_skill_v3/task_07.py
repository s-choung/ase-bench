from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk('Cu', 'fcc', a=3.61)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

ek0 = atoms.get_kinetic_energy()
ep0 = atoms.get_potential_energy()
print(ek0 + ep0)

md = VelocityVerlet(atoms, timestep=5 * units.fs)
md.run(50)

ek = atoms.get_kinetic_energy()
ep = atoms.get_potential_energy()
print(ek + ep)
