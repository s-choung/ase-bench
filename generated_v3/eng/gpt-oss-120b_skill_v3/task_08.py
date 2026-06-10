from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# Build N2 molecule and set calculator
atoms = molecule('N2')
atoms.calc = EMT()

# Geometry optimization
BFGS(atoms).run(fmax=0.01)

# Vibrational analysis
vib = Vibrations(atoms, name='n2_vib')
vib.run()
freqs = vib.get_frequencies()  # cm⁻¹

print("Vibrational frequencies (cm⁻¹):")
for f in freqs:
    print(f"{f:.2f}")

vib.clean()  # remove temporary files
