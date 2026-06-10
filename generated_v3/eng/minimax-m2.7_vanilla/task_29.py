from ase import units
from ase.lattice.cubic import FCC
from ase.calculators.emt import EMT
from ase.md import VelocityVerlet
import numpy as np

atoms = FCC('Pd', size=(2, 2, 2))
atoms.calc = EMT()

kB = units.kB
T = 500
m = atoms.get_masses()
velocities = np.random.normal(0, np.sqrt(kB * T / m[:, None]), (len(atoms), 3))
atoms.set_velocities(velocities)

dt = 2 * units.fs
dyn = VelocityVerlet(atoms, dt=dt)

E0 = atoms.get_total_energy()
dyn.run(200)
E1 = atoms.get_total_energy()

print(f'ΔE = {E1 - E0:.6f} eV')
