from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import LBFGS

atoms = bulk('Au', 'fcc', a=4.05)
atoms.calc = EMT()
opt = LBFGS(atoms)
steps = opt.run(fmax=0.01)
print(steps, atoms.get_potential_energy())
