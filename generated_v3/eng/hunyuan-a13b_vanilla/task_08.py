from ase import Atom, Molecule
from ase.vibrations import harmonic_frequencies

# Create an N2 molecule
molecule = Molecule('N2')
molecule center_of_mass = Molecule('N2', pbc=True, cell='0 0 10')
molecule center_of_mass.center(vacuum=10.0)

# Set up the EMT calculator
calculator = EMT()

# Perform geometry optimization
molecule center_of_mass.run()

# Calculate vibrational frequencies
freqs = harmonic_frequencies(molecule center_of_mass, calculator)

# Print the vibrational frequencies
print('Vibrational frequencies (cm⁻¹):')
print(freqs)
