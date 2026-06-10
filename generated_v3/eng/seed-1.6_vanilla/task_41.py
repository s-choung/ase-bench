from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.io.trajectory import Trajectory

# Create Cu FCC bulk and attach EMT calculator
atoms = bulk('Cu', 'fcc')
atoms.calc = EMT()

# Initialize velocities and MD
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
md = VelocityVerlet(atoms, timestep=1e-15)

# Save trajectory during MD
traj = Trajectory('cu_md.traj', 'w', atoms)
md.attach(traj.write, interval=1)

# Run 10 MD steps
md.run(10)

# Read trajectory and output results
traj_read = Trajectory('cu_md.traj')
print(len(traj_read), traj_read[-1].get_potential_energy())
