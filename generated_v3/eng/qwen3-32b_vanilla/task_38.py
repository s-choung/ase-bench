from ase.build import bulk
from ase.calculators.emt import EMT
from ase.thermochemistry import HarmonicThermo
from ase.phonons import Phonons

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

phonons = Phonons(atoms, supercell=(1,1,1))
phonons.run()
phonons.read()

freqs = phonons.get_frequencies()
vib_energies = freqs * 4.135667696e-3  # THz to eV

thermo = HarmonicThermo(vib_energies.flatten())
helmholtz = thermo.get_Helmholtz_energy(atoms, 300)
print(f"{helmholtz} eV")
