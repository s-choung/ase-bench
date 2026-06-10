from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS

atoms = molecule('H2O')
atoms.calc = EMT()

print(f'Before: {atoms.get_potential_energy():.6f} eV')

opt = BFGS(atoms)
opt.run(fmax=0.05)

print(f'After: {atoms.get_potential_energy():.6f} eV')
