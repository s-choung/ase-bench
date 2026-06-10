from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
atoms = Atoms('N2', positions=[(0,0,0),(0,0,1.1)])
atoms.calc = EMT()
vib = Vibrations(atoms)
vib.run()
print(vib.get_frequencies())
vib.clean()
