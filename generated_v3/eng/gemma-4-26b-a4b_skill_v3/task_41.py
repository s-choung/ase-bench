from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase.io import Trajectory, read
from ase import units

# Setup Cu FCC bulk
atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

# MD setup (NVT)
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)
dyn = Langevin(atoms, timestep=1 * units.fs, temperature_K=300, friction=0.01 / units.fs)

# Run MD and save to trajectory
traj = Trajectory('md.traj', 'w', atoms)
dyn.attach(traj.write, interval=1)
dyn.run(10)

# Read trajectory and print results
traj_read = read('md.traj', index=':')
print(f"Total frames: {len(traj_read)}")
print(f"Energy of last frame: {traj_read[-1].get_potential_energy()} eV")
