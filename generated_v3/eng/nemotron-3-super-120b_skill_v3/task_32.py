from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# Build H2O molecule
h2o = molecule('H2O')
h2o.calc = EMT()

# Optimize geometry
BFGS(h2o).run(fmax=0.05)

# Calculate vibrations
vib = Vibrations(h2o)
vib.run()

# Get frequencies (cm^-1) and energies (eV)
freqs = vib.get_frequencies()   # cm^-1
energies = vib.get_energies()   # eV

# Print results
for i, (freq, e) in enumerate(zip(freqs, energies), start=1):
    print(f'Mode {i}: {freq:8.3f} cm⁻¹   {e:8.5f} eV')

# Clean up temporary files
vib.clean()
