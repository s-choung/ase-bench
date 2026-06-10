from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS

atoms = Atoms('H2O', positions=[(0.0, 0.0, 0.0), (0.0, 0.0, 0.76), (0.0, 0.0, -0.76)])
atoms.calc = EMT()

energy_before = atoms.get_potential_energy()
print(f"Energy before optimization: {energy_before} eV")

opt = BFGS(atoms)
opt.run(fmax=0.01)

energy_after = atoms.get_potential_energy()
print(f"Energy after optimization: {energy_after} eV")
