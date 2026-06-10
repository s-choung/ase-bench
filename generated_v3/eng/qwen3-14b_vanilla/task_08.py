from ase import Atoms
from ase.calculators.emt import EMT
from ase.phonons.phonon import Phonon

n2 = Atoms('N2', positions=[(0, 0, 0), (1.1, 0, 0)])
n2.set_calculator(EMT())

phonon = Phonon(n2, n2.get_calculator())
phonon.run()

print(phonon.get_frequencies())
