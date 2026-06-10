from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import VibrationalAnalysis

atoms = Atoms('N2', positions=[[0,0,0], [0,0,1.1]], calculator=EMT())
dyn = BFGS(atoms)
dyn.run(fmax=0.01)
vib = VibrationalAnalysis(atoms)
freqs = vib.get_frequencies()
print(freqs)
