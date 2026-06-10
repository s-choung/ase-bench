from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS

molecule = Atoms('H2O', positions=[[0, 0, 0], [1, 0, 0], [0, 1, 0]])
molecule.calc = EMT()

print(f"Initial energy: {molecule.get_potential_energy():.4f} eV")

opt = BFGS(molecule)
opt.run(fmax=0.01)

print(f"Optimized energy: {molecule.get_potential_energy():.4f} eV")
