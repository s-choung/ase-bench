from ase import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS

atoms = molecule('H2O')
atoms.set_calculator(EMT())
print("Initial energy:", atoms.get_potential_energy())
opt = BFGS(atoms)
opt.optimize()
print("Final energy:", atoms.get_potential_energy())
