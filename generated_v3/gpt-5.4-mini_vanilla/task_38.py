from ase.build import bulk
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo

atoms = bulk('Cu', 'fcc', a=3.615)
atoms.calc = EMT()

vib = Vibrations(atoms)
vib.run()
freqs = vib.get_frequencies()

thermo = HarmonicThermo(vib_energies=freqs)
F = thermo.get_helmholtz_energy(temperature=300)

print("F(300 K) [eV] =", F)

vib.clean()
