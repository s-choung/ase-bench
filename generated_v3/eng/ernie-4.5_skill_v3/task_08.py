from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# Create N2 molecule
atoms = Atoms('N2', positions=[[0., 0., -0.7], [0., 0., 0.7]])

# Set EMT calculator and optimize geometry
atoms.calc = EMT()
opt = BFGS(atoms)
opt.run(fmax=0.01)  # Optimize first

# Vibrational analysis
vib = Vibrations(atoms)
vib.run()
frequencies = vib.get_frequencies()

# Print frequencies in cm⁻¹
print("Vibrational frequencies (cm⁻¹):")
for freq in frequencies:
    print(f"{freq:.2f}")

vib.clean()  # Clean up calculation files
