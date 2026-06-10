from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import LBFGS

au = bulk('Au', 'fcc', a=4.05)
au.calc = EMT()
opt = LBFGS(au)
opt.run(fmax=0.01)

print(f'Optimization steps: {opt.nsteps}')
print(f'Final energy: {au.get_potential_energy():.3f} eV')
