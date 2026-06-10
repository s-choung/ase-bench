from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.verlet import VelocityVerlet
from ase import units
import numpy as np

atoms = bulk('Pd', 'fcc', a=3.89, cubic=True).repeat((2, 2, 2))
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=500.0)

md = VelocityVerlet(atoms, timestep=2.0 * units.fs, logfile=None)

e0 = atoms.get_total_energy()

md.run(200)

e_final = atoms.get_total_energy()
print(e_final - e0)
