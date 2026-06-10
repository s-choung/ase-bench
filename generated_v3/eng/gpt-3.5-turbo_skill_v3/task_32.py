from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# Create H2O molecule
atoms = molecule('H2O')
atoms.calc = EMT()

# Optimize the structure
opt = BFGS(atoms)
opt.run(fmax=0.01)  # Optimize the structure

# Calculate the vibrational modes
vib = Vibrations(atoms)
vib.run()
freqs = vib.get_frequencies()  # Vibrational frequencies in cm^-1
energies = vib.get_energies()  # Vibrational energies in eV

for i, freq in enumerate(freqs):
    print(f'Vibrational Mode {i+1}: Frequency = {freq:.2f} cm^-1, Energy = {energies[i]:.3f} eV')

vib.clean()  # Clean up the calculations
