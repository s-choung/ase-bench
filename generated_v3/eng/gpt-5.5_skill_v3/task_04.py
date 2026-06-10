from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS

atoms = molecule("H2O")
atoms.calc = EMT()

e0 = atoms.get_potential_energy()
print(f"Energy before optimization: {e0:.6f} eV")

opt = BFGS(atoms, logfile=None)
opt.run(fmax=0.01)

e1 = atoms.get_potential_energy()
print(f"Energy after optimization:  {e1:.6f} eV")
