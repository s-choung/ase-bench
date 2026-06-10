import numpy as np
from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# Setup molecule and calculator
atoms = molecule('H2O')
atoms.calc = EMT()

# Geometry optimization is required before vibration calculation
opt = BFGS(atoms)
opt.run(fmax=0.01)

# Calculate vibrations
vib = Vibrations(atoms, name='h2o_vib')
vib.run()

# Retrieve data
freqs = vib.get_frequencies()  # in cm^-1
energies = vib.get_energies()  # in eV

# Output results
print(f"{'Mode':<10} {'Freq (cm^-1)':<15} {'Energy (eV)':<15}")
for i, (f, e) in enumerate(zip(freqs, energies)):
    print(f"{i+1:<10} {f:<15.2f} {e:<15.4f}")

# Cleanup temporary files
vib.clean()
