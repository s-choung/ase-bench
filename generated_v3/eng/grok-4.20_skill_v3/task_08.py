from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.units import Bohr

atoms = Atoms('N2', positions=[[0,0,0],[0,0,1.1]])
atoms.set_cell([10,10,10])
atoms.center()
atoms.calc = EMT()

BFGS(atoms, logfile=None).run(fmax=0.001)

vib = Vibrations(atoms, name='n2_vib', delta=0.01)
vib.run()
freqs = vib.get_frequencies()
print(freqs)
vib.clean()
