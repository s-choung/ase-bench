from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# Setup and optimize CH4
mol = molecule('CH4')
mol.calc = EMT()
opt = BFGS(mol)
opt.run(fmax=0.002)

# Calculate vibrations
vib = Vibrations(mol)
vib.run()
freqs = vib.get_frequencies()

# Filter and print real frequencies (> 0 to exclude translations/rotations)
real_freqs = [f.real for f in freqs if f.real > 1e-2]

print("Real vibrational frequencies (cm^-1):")
for f in real_freqs:
    print(f"{f:.2f}")
