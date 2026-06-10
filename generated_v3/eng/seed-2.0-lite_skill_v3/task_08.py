from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# Setup N2 molecule and calculator
atoms = molecule('N2')
atoms.calc = EMT()

# Relax structure to energy minimum before vibration calculation
BFGS(atoms).run(fmax=0.01)

# Calculate and output vibrational frequencies
vib = Vibrations(atoms)
vib.run()
frequencies = vib.get_frequencies()
print(f"Vibrational frequencies (cm⁻¹): {frequencies.round(2)}")

# Clean up temporary calculation files
vib.clean()
