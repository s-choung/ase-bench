from ase.build import bulk
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo

cu = bulk('Cu', 'fcc', a=3.6)
cu.calc = EMT()

vib = Vibrations(cu)
vib.run()
vib.summary()

freqs = vib.get_frequencies()
thermo = HarmonicThermo(vib_energies=freqs)
F = thermo.get_helmholtz_energy(temperature=300)
print(f"Helmholtz free energy at 300K: {F:.6f} eV")
