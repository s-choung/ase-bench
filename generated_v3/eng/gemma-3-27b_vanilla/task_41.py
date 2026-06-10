from ase.build import fcc111
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.verlet import VelocityVerlet
from ase import Atoms
import numpy as np

cu = fcc111('Cu', size=(2, 2, 2), vacuum=1.0)
cu.calc = ase.calculators.EMT()
cu.get_potential_energy()

vel = MaxwellBoltzmannDistribution(cu, 300)
cu.set_velocities(vel)

dyn = VelocityVerlet(cu, 0.01, trajectory='cu_md.traj')
dyn.run(10)

from ase.io import read
traj = read('cu_md.traj')
print(len(traj))
print(traj[-1].get_potential_energy())
