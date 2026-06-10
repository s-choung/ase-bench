from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
import ase.units as units

# Initialize H2O molecule with EMT calculator
atoms = molecule('H2O')
atoms.calc = EMT()

# Relax geometry to energy minimum
dyn = BFGS(atoms)
dyn.run(fmax=0.001)

# Calculate vibrational modes
vib = Vibrations(atoms)
vib.run()

# Extract and filter valid vibrational modes (exclude translation/rotation)
freqs_ev = vib.get_frequencies()
vibrational_modes = [f for f in freqs_ev if f > 0.01]  # Filter low-energy rigid body modes

# Print results
print("\nH2O Vibrational Modes (EMT):")
for idx, energy_eV in enumerate(vibrational_modes, 1):
    freq_cm = energy_eV / units.invcm
    print(f"Mode {idx}: {freq_cm:.1f} cm⁻¹ | {energy_eV:.4f} eV")

# Clean up temporary vibration files
vib.clean()
