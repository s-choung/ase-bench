from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

d = 1.1  # N-N bond length in Angstrom
atoms = Atoms('N2', positions=[[0, 0, 0], [0, 0, d]])
atoms.calc = EMT()

opt = BFGS(atoms, trajectory='opt.traj')
opt.run(fmax=0.01)

vib = Vibrations(atoms)
vib.run()
vib.summary()
print(vib.get_frequencies())
