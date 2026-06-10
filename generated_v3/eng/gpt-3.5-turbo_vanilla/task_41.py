from ase import Atoms
from ase.calculators.emt import EMT
from ase.md import MDTrajectory, Langevin

# Create Cu FCC bulk
a = 3.6
atoms = Atoms('Cu4', scaled_positions=[(0, 0, 0), (0.5, 0.5, 0), (0.5, 0, 0.5), (0, 0.5, 0.5)], cell=[a, a, a], pbc=True)

# Attach EMT calculator
atoms.set_calculator(EMT())

# Run MD for 10 steps and save to trajectory file
traj = MDTrajectory('cu_fcc.traj', mode='w', atoms=atoms)
dyn = Langevin(atoms, 1.0)
dyn.attach(traj)
dyn.run(10)

# Read trajectory back
traj = MDTrajectory('cu_fcc.traj', 'r')

# Print total number of frames and energy of the last frame
print(f"Total number of frames: {len(traj)}")
print(f"Energy of the last frame: {traj[-1].get_potential_energy()}")
