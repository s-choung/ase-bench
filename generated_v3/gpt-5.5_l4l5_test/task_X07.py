import sys
import numpy as np
from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary, ZeroRotation
from ase.io import Trajectory
from ase.geometry import find_mic

dt_fs = 5.0
nsteps = 1000
temp_K = 600.0
trajfile = "cu_fcc_3x3x3_600K.traj"

atoms = bulk("Cu", "fcc", a=3.615, cubic=True).repeat((3, 3, 3))
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=temp_K)
Stationary(atoms)
ZeroRotation(atoms)

dyn = Langevin(
    atoms,
    timestep=dt_fs * units.fs,
    temperature_K=temp_K,
    friction=0.01 / units.fs,
    trajectory=trajfile,
    logfile=None,
)
dyn.run(nsteps)

traj = Trajectory(trajfile)
frames = [a.copy() for a in traj]

temps = np.array([a.get_temperature() for a in frames])
times = np.arange(len(frames)) * dt_fs

r0 = frames[0].get_positions()
unwrapped = r0.copy()
prev = r0.copy()
msd = []

for a in frames:
    pos = a.get_positions()
    if a is frames[0]:
        disp = np.zeros_like(pos)
    else:
        d, _ = find_mic(pos - prev, a.cell, a.pbc)
        unwrapped += d
        disp = unwrapped - r0
    msd.append(np.mean(np.sum(disp**2, axis=1)))
    prev = pos.copy()

msd = np.array(msd)

print(f"Average temperature (K): {temps.mean():.6f}")
print(f"Temperature std (K): {temps.std():.6f}")
print("time_fs temperature_K MSD_A2")
np.savetxt(sys.stdout, np.column_stack((times, temps, msd)), fmt="%.8f")
