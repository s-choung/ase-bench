from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import LBFGS

au = bulk('Au', 'fcc', a=4.078)
au.calc = EMT()

dyn = LBFGS(au, trajectory='au_opt.traj')
dyn.run(fmax=0.01)

print(f"Optimization steps: {dyn.nsteps}")
print(f"Final energy: {au.get_potential_energy():.6f} eV")
