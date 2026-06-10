from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# Define CH4 molecule
atoms = Atoms('CH4',
              positions=[(0.0, 0.0, 0.0),
                         (0.629, 0.629, 0.629),
                         (-0.629, -0.629, 0.629),
                         (-0.629, 0.629, -0.629),
                         (0.629, -0.629, -0.629)])

# Set calculator
atoms.calc = EMT()

# Optimize structure
BFGS(atoms, logfile=None).run(fmax=0.05)

# Calculate vibrations
vib = Vibrations(atoms)
vib.run()

# Filter and print real frequencies (positive values in cm^-1)
real_freqs = [f for f in vib.get_frequencies() if f > 1e-3]
print("Real vibrational frequencies (cm⁻¹):")
for freq in real_freqs:
    print(f"{freq:.2f}")
