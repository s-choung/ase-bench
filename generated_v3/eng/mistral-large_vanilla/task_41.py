from ase import Atoms
from ase.calculators.emt import EMT
from ase.lattice.cubic import FaceCenteredCubic
from ase.md import VelocityVerlet
from ase import units
from ase.io import Trajectory, read

# Create Cu FCC bulk and attach EMT calculator
atoms = FaceCenteredCubic('Cu', size=(2, 2, 2))
atoms.calc = EMT()

# Run MD and save trajectory
traj = Trajectory('md.traj', 'w', atoms)
dyn = VelocityVerlet(atoms, timestep=1 * units.fs)
dyn.attach(traj.write, interval=1)
dyn.run(10)
traj.close()

# Read trajectory and print results
traj = read('md.traj', index=':')
print(len(traj), traj[-1].get_potential_energy())
