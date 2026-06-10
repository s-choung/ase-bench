from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.io import Trajectory, read
from ase import units

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.set_calculator(EMT())
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
dyn = VelocityVerlet(atoms, timestep=1 * units.fs)

with Trajectory('cu_md.traj', 'w') as traj:
    dyn.attach(traj.write, interval=1)
    dyn.run(10)

frames = read('cu_md.traj', index=':')
print(len(frames))
frames[-1].set_calculator(EMT())
print(f"{frames[-1].get_potential_energy():.4f}")
