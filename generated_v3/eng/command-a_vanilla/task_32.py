from ase import Atoms
from ase.vibrations import Vibrations
from ase.calculators.emt import EMT
import numpy as np

# Define H2O molecule
h2o = Atoms('H2O', positions=[[0, 0, 0], [0, 0.957, -0.111], [0, -0.957, -0.111]], calculator=EMT())

# Optimize geometry
h2o.get_potential_energy()

# Calculate vibrational modes
vib = Vibrations(h2o, name='H2O_vib')
vib.run()
vib.summary()

# Get vibrational frequencies in cm^-1 and energies in eV
frequencies = vib.get_frequencies()
energies = [h * f / 8065.544 for f in np.abs(frequencies)]  # h is Planck's constant in eV*s

# Print results
for i, (f, e) in enumerate(zip(np.abs(frequencies), energies)):
    print(f'Mode {i+1}: {f:.2f} cm^-1, Energy: {e:.4f} eV')
