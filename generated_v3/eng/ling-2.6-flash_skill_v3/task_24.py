from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import LBFGS
from ase.build import bulk

atoms = bulk('Au', 'fcc', a=4.08)
atoms.calc = EMT()

opt = LBFGS(atoms, trajectory='opt.traj')
steps = opt.run(fmax=0.01)
print(f'Number of steps: {steps}')
print(f'Final energy: {atoms.get_potential_energy():.6f} eV')
