from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.build import molecule
import numpy as np

# Create an H2O molecule
molecule('H2O', cut=2.21, vacuum=10.0)

# Set the EMT calculator
atoms.calc = EMT()

# Optimize the structure
try:
    BFGS(atoms).run(fmax=0.01)
except Exception as e:
    print(f"Optimization failed: {e}")
    exit()

# Run vibrations calculation
vib = Vibrations(atoms, name='vib')
vib.run()

# Print vibrational modes
for mode in vib.modes:
    freq = vib.get_frequency(mode)
    energy = vib.get_energy(mode)
    print(f"Mode: {mode}, Frequency: {freq:.2f} cm⁻¹, Energy: {energy:.6f} eV")
