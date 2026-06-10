from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# Define CH4 molecule
atoms = Atoms('CH4', positions=[
    [0, 0, 0],
    [0, 0, 1.09],
    [0.94, 0, -0.36],
    [-0.47, 0.81, -0.36],
    [-0.47, -0.81, -0.36]
])
atoms.calc = EMT()

# Geometry optimization
opt = BFGS(atoms)
opt.run(fmax=0.01)

# Vibrational calculation
vib = Vibrations(atoms)
vib.run()

# Extract real frequencies (positive values)
freqs = vib.get_frequencies()
real_freqs = sorted([f for f in freqs if f > 0])

print("Real vibrational frequencies (THz):")
for f in real_freqs:
    print(f"{f:.4f}")

vib.clean()
