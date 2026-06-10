from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.verlet import VelocityVerlet
from ase import units
from ase.io import Trajectory

# set up Cu FCC bulk
atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

# initial velocities at 300 K
MaxwellBoltzmannDistribution(atoms, temperature_K=300)

# run short MD, writing every frame
dyn = VelocityVerlet(atoms, dt=1.0 * units.fs)
with Trajectory('cu_md.traj', 'w') as traj:
    dyn.attach(traj.write, interval=1)
    dyn.run(steps=10)

# read trajectory and report
traj = Trajectory('cu_md.traj')
print('Frames:', len(traj))
last = traj[-1]
print('Energy of last frame:', last.get_potential_energy())
