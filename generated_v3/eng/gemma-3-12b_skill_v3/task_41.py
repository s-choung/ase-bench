from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.io import write, read
import numpy as np

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

md = VelocityVerlet(atoms, timestep=5*units.fs)
md.run(10)

write('md.traj', atoms)

atoms2 = read('md.traj')
num_frames = len(atoms2)
last_frame_energy = atoms2[-1].get_potential_energy() + atoms2[-1].get_kinetic_energy()

print(f"Number of frames: {num_frames}")
print(f"Energy of the last frame: {last_frame_energy}")
