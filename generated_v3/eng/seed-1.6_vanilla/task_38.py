from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Phonons
from ase.thermochemistry import HarmonicThermo

# Build and optimize Cu fcc bulk
atoms = bulk('Cu', 'fcc')
atoms.calc = EMT()
BFGS(atoms).run(fmax=0.001)

# Compute vibrational frequencies (exclude acoustic modes)
ph = Phonons(atoms, supercell=(2,2,2))
ph.run()
ph.read()
freqs = [f for f in ph.get_frequencies().flatten() if f > 1e-10]

# Calculate Helmholtz free energy at 300K
thermo = HarmonicThermo(freqs)
f_helmholtz = thermo.get_helmholtz_free_energy(300)
print(f_helmholtz)
