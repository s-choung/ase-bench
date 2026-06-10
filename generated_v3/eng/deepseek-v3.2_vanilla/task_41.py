from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.verlet import VelocityVerlet
from ase.io import write, read
from ase import units

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True) * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
dyn = VelocityVerlet(atoms, timestep=1.0 * units.fs)

traj = 'cu_md.traj'
write(traj, atoms)

for _ in range(10):
    dyn.run(1)
    write(traj, atoms, append=True)

frames = read(traj + '@:')
print(f'Total frames: {len(frames)}')
print(f'Last frame energy: {frames[-1].get_potential_energy():.4f} eV')
