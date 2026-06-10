from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS

atoms = molecule('H2O')
atoms.set_calculator(EMT())
print(atoms.get_potential_energy())
opt = BFGS(atoms)
opt.run()
print(atoms.get_potential_energy())
