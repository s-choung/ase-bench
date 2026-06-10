from ase.build import bulk
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

vib = Vibrations(atoms)
vib.run()

freqs = vib.get_frequencies()
thermo = HarmonicThermo(freqs)

F = thermo.get_helmholtz_energy(temperature=300.0)
print(f"Helmholtz free energy at 300 K: {F:.6f} eV")
