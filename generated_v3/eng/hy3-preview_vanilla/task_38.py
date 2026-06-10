from ase.build import bulk
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo
import numpy as np

# Create Cu bulk structure
atoms = bulk('Cu', 'fcc', a=3.61)

# Set calculator
atoms.calc = EMT()

# Calculate vibrations (using 2x2x2 supercell for meaningful phonons)
atoms.calc = None  # Detach calculator for vibrations
vib = Vibrations(atoms, name='vib', delta=0.05, nfree=2)
vib.run()
vib.summary(log='-')

# Get vibrational energies (in eV)
vib_energies = vib.get_energies()

# Initialize HarmonicThermo
thermo = HarmonicThermo(vib_energies)

# Calculate Helmholtz free energy at 300K
F = thermo.get_helmholtz_energy(temperature=300)

print(f"Helmholtz free energy at 300K: {F:.6f} eV")
