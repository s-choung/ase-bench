from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# Create CH4 molecule
atoms = Atoms('CH4', positions=[(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0)])

# Optimize structure
atoms.calc = EMT()
BFGS(atoms).run(fmax=0.01)

# Calculate vibrations
vib = Vibrations(atoms)
vib.run()
vib.clean()

# Filter and print real frequencies
real_freqs = [f for f in vib.get_frequencies() if f > 0]
print(f"Real frequencies (meV): {real_freqs}")
