from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import LBFGS

au = bulk('Au', 'fcc', a=4.0)
au.calc = EMT()
opt = LBFGS(au, trajectory='au.traj')
opt.run(fmax=0.01)
print(opt.get_number_of_steps(), au.get_potential_energy())
