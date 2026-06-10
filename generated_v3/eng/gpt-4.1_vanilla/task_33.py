from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# Build and set up
mol = molecule('CH4')
mol.calc = EMT()

# Optimize geometry
opt = BFGS(mol, logfile=None)
opt.run(fmax=0.02)

# Vibrational analysis
vib = Vibrations(mol)
vib.run()
freqs = vib.get_frequencies()

# Output only real frequencies
real_freqs = [f for f in freqs if abs(f.imag) < 1e-3]
print("Real vibrational frequencies (cm^-1):")
for f in real_freqs:
    print(f"{f.real:.2f}")

vib.clean()
