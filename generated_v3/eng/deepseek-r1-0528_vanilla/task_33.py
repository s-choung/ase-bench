from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# Build CH4 molecule
atoms = Atoms('CH4', positions=[
    [0, 0, 0],
    [1.1, 1.1, 0],
    [1.1, 0, 1.1],
    [0, 1.1, 1.1],
    [2.1, 0.5, 0.5]
])

# Set calculator and optimize
atoms.calc = EMT()
opt = BFGS(atoms)
opt.run(fmax=0.01)

# Perform vibration analysis
vib = Vibrations(atoms)
vib.run()
freqs = vib.get_frequencies().real

# Filter and print real frequencies (positive values)
real_freqs = [f for f in freqs if f > 0]
for freq in real_freqs:
    print(f'{freq:.2f}')
