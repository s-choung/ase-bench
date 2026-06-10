import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.phonons import Phonons
from ase.thermochemistry import HarmonicThermo

atoms = bulk('Cu', 'fcc', a=3.61)
atoms.calc = EMT()

# Use a 2x2x2 supercell for phonon calculations
ph = Phonons(atoms, supercell=(2, 2, 2))
ph.run()

# Get frequencies in eV
# ph.get_frequencies returns values in eV
frequencies = ph.get_frequencies()

# Calculate Helmholtz free energy at 300K
thermo = HarmonicThermo(frequencies, temperature=300)
f_energy = thermo.get_helmholtz_free_energy()

print(f"Helmholtz free energy at 300K: {f_energy:.4f} eV")
