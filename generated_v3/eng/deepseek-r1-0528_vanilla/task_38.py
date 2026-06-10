import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.thermochemistry import HarmonicThermo
from ase.vibrations import Vibrations

atoms = bulk('Cu', a=3.6, cubic=True)
atoms.calc = EMT()
e0 = atoms.get_potential_energy()
vib = Vibrations(atoms)
vib.run()
freqs = vib.get_frequencies()
vib.clean()

threshold = 1.0
mask = np.abs(freqs) > threshold
conversion = 1.0 / 8065.54429
energies = np.abs(freqs[mask]) * conversion

thermo = HarmonicThermo(vib_energies=energies, potentialenergy=e0)
F = thermo.get_helmholtz_energy(temperature=300.0)

print(f"{F:.6f}")
