from ase import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.io import Trajectory

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()
atoms.set_kpoint((4, 4, 4), sum=True)

with Trajectory('cu_md.traj', 'w', atoms) as traj:
    dyn = VelocityVerlet(atoms, 1e-3)
    dyn.attach(traj.write, interval=1)
    dyn.run(10)

with Trajectory('cu_md.traj', 'r') as traj:
    print(f"Frames: {len(traj)}")
    print(f"Last energy: {traj[-1].get_potential_energy()}")
