from ase import Atoms, units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.io import Trajectory

atoms = bulk('Cu','fcc',a=3.6); atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, 300)
dyn = VelocityVerlet(atoms, dt=5*units.fs, trajectory=Trajectory('md.traj','w'))
dyn.run(10)

traj = Trajectory('md.traj')
print(f"Frames: {len(traj)}")
print(f"Final energy: {traj[-1].get_potential_energy():.3f} eV")
