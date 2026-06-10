from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS

atoms = molecule('H2O')
atoms.calc = EMT()

print(f"Energy before optimization: {atoms.get_potential_energy():.4f} eV")

BFGS(atoms).run(fmax=0.01)

print(f"Energy after optimization: {atoms.get_potential_energy():.4f} eV")
