from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import LBFGS

atoms = bulk('Au', 'fcc', a=4.0)
atoms.calc = EMT()

opt = LBFGS(atoms, trajectory='opt.traj')
opt.run(fmax=0.01)

steps = len([_ for _ in Trajectory('opt.traj')])
energy = atoms.get_potential_energy()

print(steps)
print(energy)
