from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations

# Create N2 molecule
d = 1.1  # initial bond length (Å)
n2 = Atoms('N2', positions=[[0, 0, 0], [0, 0, d]])

# Set calculator
n2.calc = EMT()

# Optimize geometry
from ase.optimize import BFGS
opt = BFGS(n2)
opt.run(fmax=0.01)

# Calculate vibrations
vib = Vibrations(n2)
vib.run()

# Print frequencies
frequencies = vib.get_frequencies()
print("Vibrational frequencies (meV):")
for i, freq in enumerate(frequencies):
    print(f"Mode {i}: {freq * 1000:.2f}")
