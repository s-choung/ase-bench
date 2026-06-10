from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations

# Create N2 molecule
d = 1.10  # Approximate bond length in Angstrom
n2 = Atoms('N2', positions=[(0, 0, 0), (0, 0, d)])
n2.center(vacuum=5.0)

# Set EMT calculator
n2.calc = EMT()

# Calculate vibrational frequencies
vib = Vibrations(n2, name='vib_n2')
vib.run()
vib.summary()

# Print vibrational frequencies (in meV)
print("Vibrational frequencies (meV):")
for mode in vib.get_frequencies():
    if mode > 0:  # Only positive (real) frequencies
        print(f"{mode:.2f}")
