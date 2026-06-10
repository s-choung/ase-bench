from ase.build import molecule
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.optimize import BFGS

# Create N2 molecule and set calculator
atoms = molecule('N2')
atoms.calc = EMT()

# Optimize structure (essential before vibration analysis)
BFGS(atoms).run(fmax=0.01)

# Calculate vibrations
vib = Vibrations(atoms, name='n2_vib')
vib.run()

# Print frequencies in cm⁻¹
frequencies = vib.get_frequencies()
print(f"Vibrational frequencies (cm⁻¹): {frequencies}")

vib.clean()  # Clean up temporary files
