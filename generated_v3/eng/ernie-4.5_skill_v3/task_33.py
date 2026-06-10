from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# Create CH4 molecule
atoms = Atoms('CH4', positions=[[0, 0, 0], [1.1, 1.1, 1.1], [-1.1, -1.1, 1.1], 
                                [1.1, -1.1, -1.1], [-1.1, 1.1, -1.1]])

# Set EMT calculator
atoms.calc = EMT()

# Optimize structure
opt = BFGS(atoms)
opt.run(fmax=0.01)

# Vibrational analysis
vib = Vibrations(atoms)
vib.run()

# Get and filter real frequencies
freqs = vib.get_frequencies()
real_freqs = [f for f in freqs if f > 0]  # Only keep real (positive) frequencies

# Print results
print(f"Optimized energy: {atoms.get_potential_energy():.3f} eV")
print("Vibrational frequencies (cm⁻¹):")
for i, freq in enumerate(real_freqs, 1):
    print(f"Mode {i}: {freq:.2f}")

# Clean up calculation files
vib.clean()
