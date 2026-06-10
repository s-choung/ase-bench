from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS

atoms = Atoms('H2O', positions=[(0.0, 0.0, 0.0), (0.96, 0.0, 0.0), (-0.24, 0.93, 0.0)])
atoms.calc = EMT()

print(f"Energy before: {atoms.get_potential_energy():.6f} eV")

opt = BFGS(atoms)
opt.run(fmax=0.01)

print(f"Energy after: {atoms.get_potential_energy():.6f} eV")
