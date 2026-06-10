import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300.0, force_temp=True)

md = VelocityVerlet(atoms, timestep=5.0, trajectory=None, logfile=None)

e0 = atoms.get_potential_energy() + atoms.get_kinetic_energy()
print('Initial total energy:', e0)

md.run(steps=50)

e1 = atoms.get_potential_energy() + atoms.get_kinetic_energy()
print('Final total energy:', e1)
