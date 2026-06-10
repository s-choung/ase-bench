from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# Create and optimize N2 molecule
atoms = molecule('N2')
atoms.calc = EMT()
BFGS(atoms).run(fmax=0.01)

# Calculate vibrations and get frequencies
vib = Vibrations(atoms)
vib.run()
freqs = vib.get_frequencies()
vib.clean()

# Print non-zero frequencies
print("Vibrational frequencies (cm⁻¹):")
for freq in freqs:
    if abs(freq) > 1e-3:  # Filter out near-zero modes
        print(freq)
