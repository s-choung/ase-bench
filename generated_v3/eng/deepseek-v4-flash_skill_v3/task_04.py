from ase import units
from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS

atoms = molecule('H2O')
atoms.calc = EMT()

print(f"Energy before optimization: {atoms.get_potential_energy():.6f} eV")

opt = BFGS(atoms)
opt.run(fmax=0.01)

print(f"Energy after optimization: {atoms.get_potential_energy():.6f} eV")
