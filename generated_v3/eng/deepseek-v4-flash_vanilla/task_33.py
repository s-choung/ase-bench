from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# Create CH4 molecule
ch4 = Atoms('CH4', positions=[(0.0, 0.0, 0.0),
                               (0.0, 0.0, 1.09),
                               (1.028, 0.0, -0.363),
                               (-0.514, 0.890, -0.363),
                               (-0.514, -0.890, -0.363)])

# Set calculator
ch4.calc = EMT()

# Optimize structure
optimizer = BFGS(ch4)
optimizer.run(fmax=0.001)

# Calculate vibrations
vib = Vibrations(ch4)
vib.run()
vib.summary()

# Filter and print real frequencies
freqs = vib.get_frequencies()
real_freqs = [f for f in freqs if f != 0.0]  # Exclude zero (translation/rotation)
print("\nReal frequencies (cm^-1):")
for f in real_freqs:
    if f > 0:
        print(f"{f:.1f}")
