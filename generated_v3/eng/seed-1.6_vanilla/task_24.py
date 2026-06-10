from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import LBFGS

atoms = bulk('Au', 'fcc')
atoms.calc = EMT()
opt = LBFGS(atoms, fmax=0.01)
opt.run()
print(opt.get_number_of_steps(), atoms.get_potential_energy())
