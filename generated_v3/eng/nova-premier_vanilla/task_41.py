from ase import Atoms, units
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.verlet import VelocityVerlet
from ase.io.trajectory import Trajectory

# Create Cu FCC bulk
atoms = Atoms('Cu', cell=[3.6, 3.6, 3.6], pbc=True)
atoms *= (2, 2, 2)

# Attach EMT calculator
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, 300*units.kB)

# Save trajectory
with Trajectory('md.traj', 'w') as traj:
    dyn = VelocityVerlet(atoms, 5*units.fs)
    dyn.attach(traj.write, interval=1)
    dyn.run(10)

# Read trajectory and get properties
traj = Trajectory('md.traj')
print("Number of frames:", len(traj))
atoms = traj[-1]
print("Energy of the last frame:", atoms.get_potential_energy())
