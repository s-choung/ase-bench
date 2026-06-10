from ase import Atoms
from ase.optimize import BFGS
from ase.calculators.emt import EMT

atoms = Atoms('OH2',
              positions=[[0.0, 0.0, 0.0],
                         [0.8, 0.0, 0.0],
                         [0.0, 0.8, 0.0]])

atoms.calc = EMT()

print('Energy before:', atoms.get_potential_energy())

opt = BFGS(atoms)
opt.run(fmax=0.02)

print('Energy after: ', atoms.get_potential_energy())
