from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase import units
from ase.operators import vibrations
from ase.md.velocityverlet import VelocityVerlet
from ase.io.trajectory import Trajectory

# Build a bulk Cu structure with FCC crystal structure
atoms = bulk('Cu', 'fcc', a=3.58, cubic=True)

# Attach EMT calculator to the structure
atoms.calc = EMT()

# Save initial structure and energy
E0 = atoms.get_potential_energy()
bfgs = BFGS(atoms)
bfgs.run(fmax=0.01)

# Initialize the MD (Velocity Verlet)
v_int = vibrations.MaxwellBoltzmannDistribution(atoms, temperature_K=300)
v_int.run()
vib = vibrations.Stationary(atoms)
vib.run()

md_simulation = VelocityVerlet(atoms, timestep=5 * units.fs)
trajectory = Trajectory('md.traj', 'w')

for i in range(10):
    trajectory.write(atoms)
    md_simulation.run_step()

# Read the trajectory file and print the number of frames and energy of the last frame
md_trj = trajectory('md.traj')  # trajectory file

print(f"Total number of frames: {len(trajectoy.frames)}")

# Assuming you already know the number of frames is 10 (as MD was run for 10 steps)
last_frame = md_trj.frames[-1]
energy_last_frame = last_frame.get_potential_energy()

print(f"Energy of the last frame: {energy_last_frame}")
