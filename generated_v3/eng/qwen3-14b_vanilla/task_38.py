from ase import bulk
from ase.calculators.emt import EMT
from ase.phonons import Phonon
from ase.thermochemistry import HarmonicThermo

atoms = bulk('Cu', 'fcc', a=3.61)
atoms.calc = EMT()

phonon = Phonon(atoms)
phonon.run()

ht = HarmonicThermo(atoms, calculator='emt', temperature=300)
print(ht.get_H())
