from ase.build import bulk
from ase.calculators.emt import EMT
from ase.phonons import Phonons
from ase.thermochemistry import HarmonicThermo
import numpy as np

atoms = bulk('Cu', 'fcc', a=3.61)
atoms.calc = EMT()

ph = Phonons(atoms, 'Cu_phonon', supercell=(2, 2, 2), delta=0.02)
ph.run()
ph.read(acoustic=True)
freq = ph.get_frequencies((0, 0, 0))[3:]  # remove 3 acoustic modes ~0

energies = freq * 1.2398e-4  # THz to eV

vib_energies = np.array([e for e in energies if e > 1e-5])

thermo = HarmonicThermo(vib_energies, electronicenergy=0.0)
f = thermo.get_helmholtz_energy(temperature=300.0)

print(f'{f:.6f}')
