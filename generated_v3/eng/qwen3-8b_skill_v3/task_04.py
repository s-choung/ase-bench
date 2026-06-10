from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS

atoms = molecule('H2O')
atoms.calc = EMT()
print("Initial energy:", atoms.get_potential_energy())
opt = BFGS(atoms)
opt.run(fmax=0.05)
print("Optimized energy:", atoms.get_potential_energy())
