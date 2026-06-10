from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations

# Create water molecule
water = Atoms('H2O', positions=[[0, 0, 0], [0, 0, 1.0], [0, 1.0, 0]])

# Set up EMT calculator
calc = EMT()
water.set_calculator(calc)

# Optimize geometry to get equilibrium structure
water.set_forces([0, 0, 0])
water.optimize(tolerance=1e-6, force_tolerance=1e-5)

# Calculate vibrational modes
vib = Vibrations(water)
vib.run()

# Print vibrational mode frequencies (cm^-1) and energies (eV)
for mode in vib.results['vibrations']:
    freq_cm_1 = mode.frequency * 100  # convert to cm^-1
    energy_eV = mode.energy          # energy in eV
    print(f"Mode: {mode.index}, Frequency: {freq_cm_1:.2f} cm^-1, Energy: {energy_eV:.6f} eV")
