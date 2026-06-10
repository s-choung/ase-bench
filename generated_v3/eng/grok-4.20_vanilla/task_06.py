from ase.build import bulk
from ase.md.langevin import Langevin
from ase.units import fs, kB
import numpy as np

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms = atoms.repeat((2, 2, 2))
atoms.calc = atoms.get_calculator()  # EMT is default for Cu

print('Initial T:', atoms.get_temperature())
print('Initial E:', atoms.get_potential_energy() + atoms.get_kinetic_energy())

dyn = Langevin(atoms, timestep=5 * fs, temperature=300 * kB, friction=0.002)
dyn.run(100)

print('Final T:', atoms.get_temperature())
print('Final E:', atoms.get_potential_energy() + atoms.get_kinetic_energy())
