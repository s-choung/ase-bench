from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import LBFGS

atoms = bulk('Au', 'fcc', a=4.08)
atoms.calc = EMT()

opt = LBFGS(atoms, trajectory=None)
opt.run(fmax=0.01)

print(f"Steps: {opt.nsteps}")
print(f"Energy: {atoms.get_potential_energy():.6f} eV")
