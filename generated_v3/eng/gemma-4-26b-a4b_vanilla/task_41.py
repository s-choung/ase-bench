import numpy as np
from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.langevin import Langevin
from ase.io import Trajectory

# Setup Cu FCC bulk (Note: EMT is technically for Cu/Ni/Pd/Pt/Al, 
# but used here as requested for the specific calculator type)
atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

# Initialize MD
MaxwellBoltzmannDistribution(atoms, temperature=300)
dyn = Langevin(atoms, 1 * 1e-15, temperature=300, friction=0.01)

# Run MD and save trajectory
traj = Trajectory('md_run.traj', 'w', atoms)
dyn.attach(traj.write, interval=1)

for _ in range(10):
    dyn.step()

# Read trajectory back
traj_read = Trajectory('md_run.traj')
frames = traj_read.get_positions()
last_frame = traj_read[-1]

print(f"Total frames: {len(traj_read)}")
print(f"Energy of last frame: {last_frame.get_total_energy()} eV")
