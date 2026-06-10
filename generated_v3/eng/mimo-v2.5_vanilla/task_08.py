from ase.build import molecule
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations

# Create N2 molecule
n2 = molecule('N2')
n2.center(vacuum=2.0)

# Set up calculator
calc = EMT()
n2.calc = calc

# Calculate vibrational frequencies
vib = Vibrations(n2)
vib.run()
frequencies = vib.get_frequencies()

# Print results (in cm^-1)
print("Vibrational frequencies (cm⁻¹):")
for i, freq in enumerate(frequencies):
    if abs(freq) > 1.0:  # Filter out small numerical noise
        print(f"Mode {i+1}: {freq:.2f}")
