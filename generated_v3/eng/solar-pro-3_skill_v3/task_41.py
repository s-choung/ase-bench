import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.io.trajectory import Trajectory

# bulk Cu
Cu = bulk('Cu', 'fcc', a=3.6)          # lattice constant Å
Cu.calc = EMT()                       # attach EMT calculator

# initial geometry optimization (optional)
from ase.optimize import BFGS
opt = BFGS(Cu)
opt.run(fmax=0.05)

# set initial velocities in Maxwell–Boltzmann distribution
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
MaxwellBoltzmannDistribution(Cu, temperature_K=300)
from ase.md import minimize
minimize.run(fmax=0.01)               # ensure minimum at 300 K

# MD simulation using VelocityVerlet
steps = 10
dt = 5 * units.fs                    # time step in fs (ASE built‑in units)

with Trajectory('cu_md.traj', 'w', Cu) as traj:   # → traj.out.traj
    dyn = VelocityVerlet(Cu, timestep=dt)
    dyn.run(steps)

# read trajectory and check
traj_data = read('cu_md.traj', index=':')
print('프레임 수:', len(traj_data))
print('마지막 프레임 에너지 (eV):', traj_data[-1].get_potential_energy())
