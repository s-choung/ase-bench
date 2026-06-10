import numpy as np
from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations

# Setup N2 molecule
atoms = Atoms('N2', positions=[(0, 0, 0), (0, 0, 1.1)])
atoms.set_calculator(EMT())

# Perform geometry optimization to find equilibrium
from ase.optimize import BFGS
BFGS(atoms).run(fmax=0.01)

# Calculate vibrations
vib = Vibrations(atoms)
vib.run()
frequencies = vib.get_frequencies()

# Print only the non-zero vibrational frequency
print(f"Vibrational frequencies: {frequencies}")
print(f"Stretching frequency: {frequencies[len(frequencies)-1]:.2f} cm-1")
