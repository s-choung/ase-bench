from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations

# Create N2 molecule
atoms = Atoms('N2', positions=[(0.0, 0.0, 0.0), (0.0, 0.0, 1.1)])

# Set EMT calculator
atoms.calc = EMT()

# Calculate vibrations
vib = Vibrations(atoms)
vib.run()

# Get frequencies in cm^-1
freqs = vib.get_frequencies()
print("Vibrational frequencies (cm^-1):", freqs)
