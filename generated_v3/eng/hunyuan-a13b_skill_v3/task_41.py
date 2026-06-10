from ase import Atoms
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.io import Trajectory

# Create Cu FCC bulk structure
atoms = Atoms('Cu', cell='fcc', a=3.5668, pbc=True)

# Attach EMT calculator
atoms.calc = EMT()

# Set up MD with VelocityVerlet
md = VelocityVerlet(atoms, timestep=2 * units.fs)

# Run MD for 10 steps and save to trajectory
traj = Trajectory('md.traj', 'w', atoms)
for _ in range(10):
    md.run()
    traj.write()
traj.close()

# Read trajectory back
traj = Trajectory('md.traj', 'r')
print("Number of frames:", len(traj.images))
print("Energy of the last frame:", traj.images[-1].get_potential_energy())
