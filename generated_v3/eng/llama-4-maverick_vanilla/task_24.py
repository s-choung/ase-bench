from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import LBFGS

a = 4.08
au = Atoms('Au', positions=[[0, 0, 0]], cell=[[0.5, 0.5, 0], [0.5, 0, 0.5], [0, 0.5, 0.5]], pbc=True)
au *= (2, 2, 2)
au.calc = EMT()
opt = LBFGS(au, trajectory='au_fcc.traj')
opt.run(fmax=0.01)
print(f'Number of optimization steps: {len(opt.get_trajectory())}')
print(f'Final energy: {au.get_potential_energy()} eV')
