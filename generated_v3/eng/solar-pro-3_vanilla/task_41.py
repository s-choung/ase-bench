from ase import Atoms
from ase.calculators.emt import EMT
from ase.md.velocity Verlet import VelocityVerlet

# Cu FCC bulk
Cu = Atoms('Cu28', positions=[[0,0,0],[0.25,0.25,0.25]]*14,
           cell=(4.05,4.05,4.05), pbc=True)

# Attach EMT calculator
Cu.set_calculator(EMT())

# Write initial structure
Cu.write('init.traj')

# Set initial velocities
Cu.set_momenta(Cu.get_momenta())   # zero for static start

# Molecular dynamics
dyn = VelocityVerlet(Cu, 2.0)       # 2 fs time step
for i in range(10):
    dyn.run(1)

Cu.write('md.traj')

# Read trajectory and display statistics
from ase.io import Trajectory
traj = Trajectory('md.traj')
frames = list(traj)

print(f'Total frames: {len(frames)}')
print(f'Energy of last frame: {traj.get_frame(0).info["energy"]} eV')
