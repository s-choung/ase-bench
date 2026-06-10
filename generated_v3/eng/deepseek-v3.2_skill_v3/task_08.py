from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

atoms = Atoms('N2', positions=[[0, 0, 0], [0, 0, 1.1]])
atoms.calc = EMT()

opt = BFGS(atoms, trajectory='N2_opt.traj')
opt.run(fmax=0.001)

vib = Vibrations(atoms, name='N2_vib')
vib.run()
frequencies = vib.get_frequencies()
print(f"Vibrational frequencies: {frequencies}")
vib.summary()
vib.clean()
