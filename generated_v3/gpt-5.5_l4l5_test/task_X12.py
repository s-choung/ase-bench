from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nvtberendsen import NVTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary, ZeroRotation
from ase.io import read
from ase.io.trajectory import Trajectory
from ase import units

atoms = bulk("Cu", "fcc", a=3.6, cubic=True) * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)
ZeroRotation(atoms)

traj = Trajectory("md.traj", "w", atoms)
dyn = NVTBerendsen(atoms, timestep=1.0 * units.fs, temperature_K=300, taut=100 * units.fs)
dyn.attach(traj.write, interval=10)
dyn.run(500)
traj.close()

frames = read("md.traj", ":")
print("Number of frames:", len(frames))

last = frames[-1]
print("Last frame energy (eV):", last.get_potential_energy())
print("Last frame temperature (K):", last.get_temperature())

subset = Trajectory("subset.traj", "w")
for frame in frames[:10]:
    subset.write(frame)
subset.close()
