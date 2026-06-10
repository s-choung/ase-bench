from ase.build import bulk
from ase.optimize import LBFGS
from ase.calculators.emt import EMT

atoms = bulk('Au', crystalstructure='fcc')
atoms.set_calculator(EMT())

opt = LBFGS(atoms)
steps = opt.run(fmax=0.01)

print(f"Optimization steps: {steps}")
print(f"Final energy: {atoms.get_potential_energy():.6f} eV")
