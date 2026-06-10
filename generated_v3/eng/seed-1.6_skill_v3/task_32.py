from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# Build and optimize H2O
h2o = molecule('H2O')
h2o.calc = EMT()
BFGS(h2o).run(fmax=0.01)

# Calculate vibrations
vib = Vibrations(h2o)
vib.run()

# Extract and print data
freqs = vib.get_frequencies()
energies = vib.get_energies()
for idx, (freq, energy) in enumerate(zip(freqs, energies), 1):
    print(f'Mode {idx}: {freq:.2f} cm⁻¹, {energy:.6f} eV')

vib.clean()
