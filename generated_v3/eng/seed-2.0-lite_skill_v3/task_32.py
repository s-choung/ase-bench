from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# Initialize H2O molecule and assign calculator
atoms = molecule('H2O')
atoms.calc = EMT()

# Relax structure first (required for vibration calculations)
opt = BFGS(atoms)
opt.run(fmax=0.01)

# Calculate vibrational modes
vib = Vibrations(atoms)
vib.run()
frequencies = vib.get_frequencies()  # Units: cm⁻¹
energies = vib.get_energies()        # Units: eV

# Print results for all vibrational modes
for idx, (freq, energy) in enumerate(zip(frequencies, energies), 1):
    print(f"Mode {idx}: {freq:.2f} cm⁻¹ | {energy:.4f} eV")

# Clean up temporary vibration calculation files
vib.clean()
