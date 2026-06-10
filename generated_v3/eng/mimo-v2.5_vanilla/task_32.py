from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
import numpy as np

# Create H2O molecule
h2o = Atoms('H2O', positions=[[0, 0, 0], [0.76, 0.59, 0], [-0.76, 0.59, 0]])

# Calculate vibrations
h2o.calc = EMT()
vib = Vibrations(h2o, name='vib_H2O')
vib.run()

# Get frequencies (THz) and convert to cm^-1
frequencies_THz = vib.get_frequencies()
frequencies_cm1 = frequencies_THz * 33.356  # 1 THz = 33.356 cm^-1

# Calculate energies (eV) using E = h * ν
# h = 4.135667662e-15 eV·s, ν = frequencies_THz × 1e12 Hz
energies_eV = frequencies_THz * 1e12 * 4.135667662e-15

# Print results
print("Vibrational Modes of H2O:")
for i, (freq_cm1, energy_eV) in enumerate(zip(frequencies_cm1, energies_eV)):
    print(f"Mode {i+1}: {freq_cm1:.1f} cm^-1, {energy_eV:.6f} eV")

vib.clean()
