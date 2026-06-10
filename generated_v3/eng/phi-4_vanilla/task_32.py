from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations

# Define an H2O molecule in a relaxed and simple configuration
water = Atoms('H2O', positions=[[0, 0, 0.757160], [0, 0, -0.757160]])
water.set_cell([[1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0]])

# Use the EMT calculator
calc = EMT()
water.set_calculator(calc)

# Calculate the phonon frequencies using the Vibrations class
vib = Vibrations(water)
ph = vib.get_phonons()

# Run the calculations
water.get_potential_energy()
ph.calculation()

# Output the vibrational modes
for mode in ph.frequencies:
    freq_cm = mode.frequency / vib.constants.c * vib.constants.vac2ev  # Convert frequency to cm-1
    energy = mode.energy  # Energy in eV
    print(f"Frequency: {freq_cm:.3f} cm^-1, Energy: {energy:.3f} eV")
