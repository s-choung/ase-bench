from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import QuasiNewton
from ase.vibrations import Vibrations

# Create N2 molecule
d = 1.10  # Approximate bond length for N2
n2 = Atoms('N2', positions=[(0, 0, 0), (d, 0, 0)])

# Attach EMT calculator
n2.calc = EMT()

# Optimize the geometry
qn = QuasiNewton(n2)
qn.run(fmax=0.001)

# Calculate vibrational frequencies
vib = Vibrations(n2)
vib.run()
vib.summary()

# Print vibrational frequencies in cm^-1
print("Vibrational Frequencies (in cm^-1):")
for freq in vib.get_frequencies():
    print(f"{freq:.2f}")
