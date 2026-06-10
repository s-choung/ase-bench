from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import LBFGS

au = bulk('Au', 'fcc')
au.calc = EMT()

opt = LBFGS(au)
opt.run(fmax=0.01)

print(f"Steps: {opt.nsteps}")
print(f"Final energy: {au.get_potential_energy():.6f} eV")
