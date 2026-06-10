from ase.build import molecule
from ase.calculators.morse import MorsePotential
from ase.optimize import BFGS
from ase.vibrations import Vibrations
import numpy as np

# Create H2O molecule
atoms = molecule('H2O')

# Set calculator (Morse potential works for H2O, EMT doesn't support H/O)
atoms.calc = MorsePotential()

# Optimize geometry
opt = BFGS(atoms)
opt.run(fmax=0.01)

# Calculate vibrations
vib = Vibrations(atoms)
vib.run()

# Get frequencies (cm^-1) and energies (eV)
frequencies = vib.get_frequencies()
energies = vib.get_energies()

# Print results
print("Vibrational modes of H2O:")
print(f"{'Mode':<5} {'Frequency (cm^-1)':<20} {'Energy (eV)':<15}")
print("-" * 45)
for i, (freq, en) in enumerate(zip(frequencies, energies)):
    print(f"{i+1:<5} {freq:<20.2f} {en:<15.6f}")

# Clean up vibration calculation files
vib.clean()
