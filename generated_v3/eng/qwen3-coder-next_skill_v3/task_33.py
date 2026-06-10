from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# Create CH4 molecule
atoms = Atoms('CH4', positions=[
    [0.0, 0.0, 0.0],  # C
    [0.629, 0.629, 0.629],
    [-0.629, -0.629, 0.629],
    [-0.629, 0.629, -0.629],
    [0.629, -0.629, -0.629]
])

# Set calculator
atoms.calc = EMT()

# Optimize structure
BFGS(atoms).run(fmax=0.01)

# Calculate vibrations
vib = Vibrations(atoms, name='ch4_vib')
vib.run()

# Get real frequencies (filter imaginary frequencies)
freqs = vib.get_frequencies()
real_freqs = [f for f in freqs if abs(f.imag) < 0.1]
real_freqs = [round(f.real, 2) for f in real_freqs]

# Print real frequencies
print("Real vibrational frequencies (cm⁻¹):", real_freqs)

# Clean up
vib.clean()
