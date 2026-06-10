from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import LBFGS
from ase.io.trajectory import Trajectory

atoms = bulk('Au', 'fcc', a=4.08)
atoms.calc = EMT()
traj = Trajectory('opt.traj', 'w', atoms)
opt = LBFGS(atoms, trajectory=traj)
opt.run(fmax=0.01)
print(f"Steps: {len(traj)}")
print(f"Final energy: {atoms.get_potential_energy():.6f} eV")
