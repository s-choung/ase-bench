from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import LBFGS

atoms = bulk('Au', 'fcc', a=4.08)
atoms.calc = EMT()
opt = LBFGS(atoms)
opt.run(fmax=0.01)
print("Steps:", opt.nsteps)
print("Final energy (eV):", atoms.get_potential_energy())
