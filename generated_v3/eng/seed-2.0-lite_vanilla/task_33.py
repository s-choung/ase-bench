from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# Initialize CH4 molecule with EMT calculator
atoms = molecule('CH4')
atoms.calc = EMT()

# Optimize geometry to energy minimum
dyn = BFGS(atoms)
dyn.run(fmax=0.01)

# Calculate vibrational modes
vib = Vibrations(atoms)
vib.run()

# Extract and filter real (positive, non-translational/rotational) frequencies
all_freqs = vib.get_frequencies()
real_freqs = [round(f, 2) for f in all_freqs if f > 1e-2]

# Print results
print(f"Number of real vibrational frequencies: {len(real_freqs)}")
print(f"Real vibrational frequencies (cm⁻¹): {real_freqs}")
