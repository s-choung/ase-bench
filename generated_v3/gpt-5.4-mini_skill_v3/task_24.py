from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import LBFGS

atoms = bulk('Au', 'fcc', a=4.08, cubic=True)
atoms.calc = EMT()

opt = LBFGS(atoms, trajectory='au_opt.traj')
nsteps = opt.run(fmax=0.01)

print(f"Optimization steps: {nsteps}")
print(f"Final energy (eV): {atoms.get_potential_energy():.6f}")
