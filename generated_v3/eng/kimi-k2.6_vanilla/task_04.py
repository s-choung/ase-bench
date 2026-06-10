from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS

mol = Atoms('H2O', positions=[[0, 0, 0], [0.96, 0, 0], [-0.24, 0.93, 0]])
mol.calc = EMT()

print('Energy before:', mol.get_potential_energy())

opt = BFGS(mol)
opt.run(fmax=0.05)

print('Energy after:', mol.get_potential_energy())
