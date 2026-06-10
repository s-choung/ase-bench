from ase.build import fcc_crystal
from ase.calculators.emt import EMT
from ase.md.velocity import Velocity
from ase.io import write, read

atoms = fcc_crystal('Cu', size=(2, 2, 2))
calc = EMT()
atoms.set_calculator(calc)

dyn = Velocity(atoms, dt=0.01)
dyn.run(10)

write('trajectory.traj', atoms)

traj = read('trajectory.traj')
num_frames = len(traj)
last_atoms = traj[-1]
energy = last_atoms.get_potential_energy()

print(f"Number of frames: {num_frames}")
print(f"Energy of the last frame: {energy}")
