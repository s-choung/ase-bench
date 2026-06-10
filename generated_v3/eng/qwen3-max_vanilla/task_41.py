from ase import Atoms
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.io import read, write
from ase.build import bulk
import numpy as np

# Create Cu FCC bulk
atoms = bulk('Cu', 'fcc', a=3.6)

# Attach EMT calculator
atoms.calc = EMT()

# Run MD for 10 steps
dyn = VelocityVerlet(atoms, timestep=1.0)
traj_file = 'cu_md.traj'
dyn.attach(write, interval=1, filename=traj_file)
for _ in range(10):
    dyn.run(1)

# Read trajectory
traj = read(traj_file, index=':')
print(len(traj))
print(traj[-1].get_potential_energy())
