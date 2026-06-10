from ase.build import bulk
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo

# Build Cu bulk (fcc)
atoms = bulk('Cu', 'fcc', a=3.615)
atoms.calc = EMT()

# Calculate vibrational frequencies
vib = Vibrations(atoms)
vib.run()
vib.summary()

# Harmonic thermochemistry at 300 K
thermo = HarmonicThermo(vib, temperature=300.0)
F = thermo.get_helmholtz_energy()
print(f"Helmholtz free energy at 300 K: {F:.4f} eV")
