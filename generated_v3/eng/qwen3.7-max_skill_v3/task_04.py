from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS

atoms = molecule('H2O')
atoms.calc = EMT()

e_before = atoms.get_potential_energy()
print(f"Energy before optimization: {e_before:.4f} eV")

opt = BFGS(atoms)
opt.run(fmax=0.01)

e_after = atoms.get_potential_energy()
print(f"Energy after optimization: {e_after:.4f} eV")
